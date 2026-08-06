import pytest
from unittest.mock import patch
from content import conclave
from models.domain import CheckResult, Player, Family


def _player() -> Player:
    family = Family(name="Test", city="Roma", multipliers=[1.0, 1.0, 1.0, 1.0, 1.0])
    return Player(name="X", family=family, voc=10, pop_agr=10, pol_infl=10, cur_rel=10, dipl_skill=10)


class TestRunMission:
    """Unit tests for the generic _run_mission helper that every conclave
    mission now goes through: it shows a real numbered choice, invokes the
    matching skill check with the approach's threshold modifier, and applies
    a stat bonus/penalty when the chosen approach was bold."""

    @patch("builtins.input", return_value="1")
    @patch("content.conclave.ui")
    @patch("content.conclave.skill_check")
    def test_safe_approach_uses_safe_modifier_and_grants_no_bonus(self, mock_skill_check, mock_ui, mock_input):
        mock_skill_check.faith.return_value = CheckResult.SUCCESS
        player = _player()
        approaches = [conclave.Approach("faith", bold=False, stat="voc")]

        success = conclave._run_mission(player, {}, "spanish_alliance_mission_1", approaches)

        assert success is True
        _, kwargs = mock_skill_check.faith.call_args
        assert kwargs["threshold_modifier"] == conclave.SAFE_MODIFIER
        assert player.voc == 10
        mock_ui.print_points.assert_not_called()

    @patch("builtins.input", return_value="1")
    @patch("content.conclave.ui")
    @patch("content.conclave.skill_check")
    def test_bold_approach_success_grants_bonus_and_shows_points(self, mock_skill_check, mock_ui, mock_input):
        mock_skill_check.faith.return_value = CheckResult.SUCCESS
        player = _player()
        approaches = [conclave.Approach("faith", bold=True, stat="voc")]

        success = conclave._run_mission(player, {}, "spanish_alliance_mission_1", approaches)

        assert success is True
        _, kwargs = mock_skill_check.faith.call_args
        assert kwargs["threshold_modifier"] == conclave.BOLD_MODIFIER
        assert player.voc == 10 + conclave.BOLD_BONUS
        mock_ui.print_points.assert_called_once_with(player)

    @patch("builtins.input", return_value="1")
    @patch("content.conclave.ui")
    @patch("content.conclave.skill_check")
    def test_bold_approach_failure_applies_penalty(self, mock_skill_check, mock_ui, mock_input):
        mock_skill_check.faith.return_value = CheckResult.FAILURE
        player = _player()
        approaches = [conclave.Approach("faith", bold=True, stat="voc")]

        success = conclave._run_mission(player, {}, "spanish_alliance_mission_1", approaches)

        assert success is False
        assert player.voc == 10 - conclave.BOLD_PENALTY
        mock_ui.print_points.assert_called_once_with(player)

    @patch("builtins.input", side_effect=["9", "abc", "2"])
    @patch("content.conclave.ui")
    @patch("content.conclave.skill_check")
    def test_invalid_choices_reprompt_until_a_valid_one_is_given(self, mock_skill_check, mock_ui, mock_input):
        mock_skill_check.secrets.return_value = CheckResult.SUCCESS
        player = _player()
        approaches = [
            conclave.Approach("faith", bold=False, stat="voc"),
            conclave.Approach("secrets", bold=False, stat="pol_infl"),
        ]

        success = conclave._run_mission(player, {}, "spanish_alliance_mission_1", approaches)

        assert success is True
        assert mock_ui.error.call_count == 2
        mock_skill_check.secrets.assert_called_once()
        mock_skill_check.faith.assert_not_called()

    def test_invoke_check_dispatches_to_the_matching_engine_method(self):
        with patch("content.conclave.skill_check") as mock_skill_check:
            player = _player()
            conclave._invoke_check("faith", player, {}, 5)
            conclave._invoke_check("secrets", player, {}, 5)
            conclave._invoke_check("influence", player, {}, 5)
            conclave._invoke_check("strategy", player, {}, 5)
            conclave._invoke_check("charisma", player, {}, 5)

        mock_skill_check.faith.assert_called_once_with(player.voc, {}, threshold_modifier=5)
        mock_skill_check.secrets.assert_called_once_with({}, threshold_modifier=5)
        mock_skill_check.influence.assert_called_once_with(player.pol_infl, {}, threshold_modifier=5)
        mock_skill_check.strategy.assert_called_once_with({}, threshold_modifier=5)
        mock_skill_check.charisma.assert_called_once_with(player.dipl_skill, {}, threshold_modifier=5)


class TestRunSpanishAlliance:
    # With input() always returning "1", each mission resolves to its first
    # approach: mission 1 -> faith, mission 2 -> charisma, mission 3 -> influence.

    @patch("builtins.input", return_value="1")
    @patch("content.conclave.run_pope_nomination")
    @patch("content.conclave.ui")
    @patch("content.conclave.skill_check")
    @patch("data.repositories.cardinal_repo.get_all_dict", return_value={})
    def test_all_successes_reach_pope_nomination(
        self, mock_cards, mock_skill_check, mock_ui, mock_nomination, mock_input
    ):
        mock_skill_check.faith.return_value = CheckResult.SUCCESS
        mock_skill_check.charisma.return_value = CheckResult.SUCCESS
        mock_skill_check.influence.return_value = CheckResult.SUCCESS

        conclave.run_spanish_alliance(_player())

        mock_nomination.assert_called_once()
        mock_ui.gameover.assert_not_called()

    @patch("builtins.input", return_value="1")
    @patch("content.conclave.ui")
    @patch("content.conclave.skill_check")
    @patch("data.repositories.cardinal_repo.get_all_dict", return_value={})
    def test_all_failures_end_in_gameover(self, mock_cards, mock_skill_check, mock_ui, mock_input):
        mock_skill_check.faith.return_value = CheckResult.FAILURE
        mock_skill_check.charisma.return_value = CheckResult.FAILURE
        mock_skill_check.influence.return_value = CheckResult.FAILURE

        conclave.run_spanish_alliance(_player())

        mock_ui.gameover.assert_called_once()


class TestRunPersonalAlliance:
    # mission 1 -> faith, mission 2 -> influence, mission 3 -> faith.

    @patch("builtins.input", return_value="1")
    @patch("content.conclave.run_alliance_consensus")
    @patch("content.conclave.ui")
    @patch("content.conclave.skill_check")
    @patch("data.repositories.cardinal_repo.get_all_dict", return_value={})
    def test_two_successes_reach_next_stage(self, mock_cards, mock_skill_check, mock_ui, mock_next_stage, mock_input):
        mock_skill_check.faith.side_effect = [CheckResult.SUCCESS, CheckResult.SUCCESS]
        mock_skill_check.influence.return_value = CheckResult.FAILURE

        conclave.run_personal_alliance(_player())

        mock_next_stage.assert_called_once()
        mock_ui.gameover.assert_not_called()


class TestRunAllianceConsensus:
    # mission 1 -> secrets, mission 2 -> influence, mission 3 -> faith.

    @patch("builtins.input", return_value="1")
    @patch("content.conclave.run_pope_nomination")
    @patch("content.conclave.ui")
    @patch("content.conclave.skill_check")
    @patch("data.repositories.cardinal_repo.get_all_dict", return_value={})
    def test_two_successes_reach_pope_nomination_without_recursing(
        self, mock_cards, mock_skill_check, mock_ui, mock_nomination, mock_input
    ):
        mock_skill_check.secrets.return_value = CheckResult.SUCCESS
        mock_skill_check.influence.return_value = CheckResult.SUCCESS
        mock_skill_check.faith.return_value = CheckResult.FAILURE

        conclave.run_alliance_consensus(_player())

        assert mock_skill_check.secrets.call_count == 1
        assert mock_skill_check.influence.call_count == 1
        mock_nomination.assert_called_once()
        mock_ui.gameover.assert_not_called()
