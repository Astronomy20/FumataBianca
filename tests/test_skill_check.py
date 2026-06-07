import pytest
from unittest.mock import patch, MagicMock
from models.domain import Cardinal, CheckResult
from systems.skill_check import SkillCheckEngine
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
