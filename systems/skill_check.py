import random
import shutil
import textwrap
from typing import Dict

from models.domain import Cardinal, CheckResult
from systems.dice import dice
from core.localization import loc


def _print(text: str) -> None:
    width = shutil.get_terminal_size().columns
    for paragraph in text.split("\n"):
        formatted_text = textwrap.fill(paragraph, width=width)
        print(formatted_text)


class SkillCheckEngine:
    def faith(self, voc: int, cardinals_dict: Dict[str, Cardinal]) -> CheckResult:
        random_cardinals = random.sample(list(cardinals_dict.keys()), random.randint(2, 3))
        belief = 0

        for name in random_cardinals:
            belief += cardinals_dict[name].voc

        _print(loc.get("faith_test", faith=belief))

        _print(loc.get("test_input_1"))
        input()
        dice.roll(6)
        result1 = dice.roll(6)
        _print(loc.get("test_result", result=result1 * 2))

        _print(loc.get("test_input_2"))
        input()
        dice.roll(4)
        result2 = dice.roll(4)
        _print(loc.get("test_result", result=result2 * 3))

        player_score = voc + result1 * 2 + result2 * 3

        if player_score >= belief:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE

    def secrets(self, cardinals_dict: Dict[str, Cardinal]) -> CheckResult:
        random_value = random.randint(10, 15)

        _print(loc.get("secrets_test", secrets=random_value))

        _print(loc.get("test_input_3"))
        input()
        dice.roll(6)
        result1 = dice.roll(6)
        _print(loc.get("test_result", result=result1))

        _print(loc.get("test_input_4"))
        input()
        dice.roll(4)
        result2 = dice.roll(4)
        _print(loc.get("test_result", result=result2 * 2))

        player_score = result1 + result2 * 2

        if player_score >= random_value:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE

    def influence(self, pol_infl: int, cardinals_dict: Dict[str, Cardinal]) -> CheckResult:
        random_cardinals = random.sample(list(cardinals_dict.keys()), random.randint(2, 3))
        belief = 0

        for name in random_cardinals:
            belief += cardinals_dict[name].pop_agr

        _print(loc.get("influence_test", belief=belief))

        _print(loc.get("test_input_1"))
        input()
        dice.roll(6)
        result1 = dice.roll(6)
        _print(loc.get("test_result", result=result1 * 2))

        _print(loc.get("test_input_2"))
        input()
        dice.roll(4)
        result2 = dice.roll(4)
        _print(loc.get("test_result", result=result2 * 3))

        player_score = pol_infl + result1 * 2 + result2 * 3

        if player_score >= belief:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE

    def strategy(self, cardinals_dict: Dict[str, Cardinal]) -> CheckResult:
        random_value = random.randint(10, 20)

        _print(loc.get("strategy_test", strategy=random_value))

        _print(loc.get("test_input_1"))
        input()
        dice.roll(6)
        result1 = dice.roll(6)
        _print(loc.get("test_result", result=result1 * 2))

        _print(loc.get("test_input_2"))
        input()
        dice.roll(4)
        result2 = dice.roll(4)
        _print(loc.get("test_result", result=result2 * 3))

        player_score = result1 * 2 + result2 * 3

        if player_score >= random_value:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE

    def charisma(self, dipl_skill: int, cardinals_dict: Dict[str, Cardinal]) -> CheckResult:
        random_cardinals = random.sample(list(cardinals_dict.keys()), 2)
        belief = 0

        for name in random_cardinals:
            belief += cardinals_dict[name].dipl_skill

        _print(loc.get("charisma_test", charisma=belief))

        _print(loc.get("test_input_3"))
        input()
        dice.roll(6)
        result1 = dice.roll(6)
        _print(loc.get("test_result", result=result1 * 1))

        _print(loc.get("test_input_4"))
        input()
        dice.roll(4)
        result2 = dice.roll(4)
        _print(loc.get("test_result", result=result2 * 2))

        player_score = dipl_skill + result1 * 2 + result2 * 3

        if player_score >= belief:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE


skill_check = SkillCheckEngine()
