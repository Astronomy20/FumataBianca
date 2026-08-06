import pytest
from unittest.mock import patch, MagicMock
from models.domain import Cardinal, CheckResult
from systems.skill_check import SkillCheckEngine
from systems import skill_check as skill_check_module
from core.localization import Localization


def _make_cardinals(n: int = 5) -> dict:
    return {
        f"C{i}": Cardinal(name=f"C{i}", voc=7, pop_agr=7, pol_infl=7, cur_rel=7, dipl_skill=7)
        for i in range(n)
    }


@pytest.fixture(autouse=True)
def load_lang():
    Localization().load("en")


class TestFaithCheck:
    def setup_method(self):
        self.engine = SkillCheckEngine()
        self.cards = _make_cardinals()

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_high_rolls_succeed(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.sample.return_value = ["C0", "C1"]
            mock_rand.randint.return_value = 2
            mock_dice.roll.return_value = 6
            result = self.engine.faith(voc=50, cardinals_dict=self.cards)
        assert result == CheckResult.SUCCESS

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_low_rolls_fail(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.sample.return_value = ["C0", "C1", "C2"]
            mock_rand.randint.return_value = 3
            mock_dice.roll.return_value = 1
            result = self.engine.faith(voc=0, cardinals_dict=self.cards)
        assert result == CheckResult.FAILURE

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_returns_check_result_type(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.sample.return_value = ["C0"]
            mock_rand.randint.return_value = 1
            mock_dice.roll.return_value = 3
            result = self.engine.faith(voc=5, cardinals_dict=self.cards)
        assert isinstance(result, CheckResult)

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_positive_threshold_modifier_makes_the_check_harder(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.sample.return_value = ["C0", "C1"]
            mock_rand.randint.return_value = 2
            mock_dice.roll.return_value = 3
            # player_score = 5 + (3+3) + (3+3+3) = 20; belief without modifier = 14 (7+7)
            result = self.engine.faith(voc=5, cardinals_dict=self.cards, threshold_modifier=10)
        assert result == CheckResult.FAILURE

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_negative_threshold_modifier_makes_the_check_easier(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.sample.return_value = ["C0", "C1"]
            mock_rand.randint.return_value = 2
            mock_dice.roll.return_value = 1
            # player_score = 0 + (1+1) + (1+1+1) = 5; belief without modifier = 14 (7+7)
            result = self.engine.faith(voc=0, cardinals_dict=self.cards, threshold_modifier=-10)
        assert result == CheckResult.SUCCESS

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_rolls_two_d6_and_three_d4_as_real_separate_dice(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.sample.return_value = ["C0", "C1"]
            mock_rand.randint.return_value = 2
            mock_dice.roll.return_value = 3
            self.engine.faith(voc=0, cardinals_dict=self.cards)
        assert mock_dice.roll.call_count == 5  # 2 d6 + 3 d4, not one roll scaled up
        mock_dice.animate_multiple.assert_any_call(6, 2)
        mock_dice.animate_multiple.assert_any_call(4, 3)


class TestSecretsCheck:
    def setup_method(self):
        self.engine = SkillCheckEngine()
        self.cards = _make_cardinals()

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_high_rolls_succeed(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.randint.return_value = 10
            mock_dice.roll.return_value = 6
            result = self.engine.secrets(cardinals_dict=self.cards)
        assert result == CheckResult.SUCCESS

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_returns_check_result_type(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.randint.return_value = 12
            mock_dice.roll.return_value = 2
            result = self.engine.secrets(cardinals_dict=self.cards)
        assert isinstance(result, CheckResult)

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_threshold_modifier_shifts_the_random_threshold(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.randint.return_value = 10
            mock_dice.roll.return_value = 3
            # player_score = 3 + (3+3) = 9; a +10 modifier pushes the threshold out of reach
            result = self.engine.secrets(cardinals_dict=self.cards, threshold_modifier=10)
        assert result == CheckResult.FAILURE

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_rolls_one_d6_and_two_d4_as_real_separate_dice(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.randint.return_value = 10
            mock_dice.roll.return_value = 3
            self.engine.secrets(cardinals_dict=self.cards)
        assert mock_dice.roll.call_count == 3  # 1 d6 + 2 d4


class TestInfluenceCheck:
    def setup_method(self):
        self.engine = SkillCheckEngine()
        self.cards = _make_cardinals()

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_uses_pop_agr_for_belief(self, mock_print, mock_input):
        cards = {
            "A": Cardinal("A", voc=10, pop_agr=5, pol_infl=10, cur_rel=10, dipl_skill=10),
            "B": Cardinal("B", voc=10, pop_agr=5, pol_infl=10, cur_rel=10, dipl_skill=10),
        }
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.sample.return_value = ["A", "B"]
            mock_rand.randint.return_value = 2
            mock_dice.roll.return_value = 6
            result = self.engine.influence(pol_infl=50, cardinals_dict=cards)
        assert result == CheckResult.SUCCESS


class TestStrategyCheck:
    def setup_method(self):
        self.engine = SkillCheckEngine()
        self.cards = _make_cardinals()

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_returns_check_result(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.randint.return_value = 15
            mock_dice.roll.return_value = 4
            result = self.engine.strategy(cardinals_dict=self.cards)
        assert isinstance(result, CheckResult)


class TestCharismaCheck:
    def setup_method(self):
        self.engine = SkillCheckEngine()
        self.cards = _make_cardinals()

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_samples_exactly_two_cardinals(self, mock_print, mock_input):
        sampled = []
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            def capture_sample(population, k):
                sampled.append(k)
                return list(self.cards.keys())[:k]
            mock_rand.sample.side_effect = capture_sample
            mock_rand.randint = MagicMock(return_value=2)
            mock_dice.roll.return_value = 3
            self.engine.charisma(dipl_skill=5, cardinals_dict=self.cards)
        assert sampled and sampled[0] == 2

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_uses_one_d6_and_two_d4_like_its_own_prompts_say(self, mock_print, mock_input):
        # Regression test: charisma used to reuse the "two d6 + three d4"
        # weighting from faith/influence/strategy while still showing the
        # "one d6 + two d4" prompts (test_input_3/4) borrowed from secrets,
        # so a single d6 roll could be displayed as e.g. "You rolled 10!" —
        # impossible on a 6-sided die. It must match secrets' dice count.
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.sample.return_value = ["C0", "C1"]
            mock_dice.roll.return_value = 3
            self.engine.charisma(dipl_skill=0, cardinals_dict=self.cards)
        assert mock_dice.roll.call_count == 3  # 1 d6 + 2 d4, not 2 d6 + 3 d4

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_player_score_is_the_real_sum_of_the_rolled_dice(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice, \
             patch("systems.skill_check.random") as mock_rand:
            mock_rand.sample.return_value = ["C0", "C1"]  # belief = 7 + 7 = 14
            mock_dice.roll.side_effect = [6, 4, 4]  # 1 d6=6, 2 d4=[4, 4]
            # player_score = dipl_skill(0) + 6 + (4 + 4) = 14 >= belief(14)
            result = self.engine.charisma(dipl_skill=0, cardinals_dict=self.cards)
        assert result == CheckResult.SUCCESS


class TestRollGroup:
    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_returns_the_sum_of_distinct_individual_rolls(self, mock_print, mock_input):
        with patch("systems.skill_check.dice") as mock_dice:
            mock_dice.roll.side_effect = [2, 5, 6]
            total = skill_check_module._roll_group(6, 3)
        assert total == 13  # 2 + 5 + 6, not one roll scaled by 3
        mock_dice.animate_multiple.assert_called_once_with(6, 3)
        mock_dice.render_faces.assert_called_once_with(6, [2, 5, 6])
