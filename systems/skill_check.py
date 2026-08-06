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


def _roll_group(faces: int, count: int) -> int:
    """Roll `count` dice of `faces` sides together, animate and show them
    side by side (each with its own correct face), and return their sum —
    the actual sum of that many real dice, not a single roll scaled up."""
    input()
    dice.animate_multiple(faces, count)
    results = [dice.roll(faces) for _ in range(count)]
    dice.render_faces(faces, results)
    total = sum(results)
    _print(loc.get("test_result", result=total))
    return total


class SkillCheckEngine:
    def faith(self, voc: int, cardinals_dict: Dict[str, Cardinal], threshold_modifier: int = 0) -> CheckResult:
        random_cardinals = random.sample(list(cardinals_dict.keys()), random.randint(2, 3))
        belief = threshold_modifier

        for name in random_cardinals:
            belief += cardinals_dict[name].voc

        _print(loc.get("faith_test", faith=belief))

        _print(loc.get("test_input_1"))
        result1 = _roll_group(6, 2)

        _print(loc.get("test_input_2"))
        result2 = _roll_group(4, 3)

        player_score = voc + result1 + result2

        if player_score >= belief:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE

    def secrets(self, cardinals_dict: Dict[str, Cardinal], threshold_modifier: int = 0) -> CheckResult:
        random_value = random.randint(10, 15) + threshold_modifier

        _print(loc.get("secrets_test", secrets=random_value))

        _print(loc.get("test_input_3"))
        result1 = _roll_group(6, 1)

        _print(loc.get("test_input_4"))
        result2 = _roll_group(4, 2)

        player_score = result1 + result2

        if player_score >= random_value:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE

    def influence(self, pol_infl: int, cardinals_dict: Dict[str, Cardinal], threshold_modifier: int = 0) -> CheckResult:
        random_cardinals = random.sample(list(cardinals_dict.keys()), random.randint(2, 3))
        belief = threshold_modifier

        for name in random_cardinals:
            belief += cardinals_dict[name].pop_agr

        _print(loc.get("influence_test", belief=belief))

        _print(loc.get("test_input_1"))
        result1 = _roll_group(6, 2)

        _print(loc.get("test_input_2"))
        result2 = _roll_group(4, 3)

        player_score = pol_infl + result1 + result2

        if player_score >= belief:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE

    def strategy(self, cardinals_dict: Dict[str, Cardinal], threshold_modifier: int = 0) -> CheckResult:
        random_value = random.randint(10, 20) + threshold_modifier

        _print(loc.get("strategy_test", strategy=random_value))

        _print(loc.get("test_input_1"))
        result1 = _roll_group(6, 2)

        _print(loc.get("test_input_2"))
        result2 = _roll_group(4, 3)

        player_score = result1 + result2

        if player_score >= random_value:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE

    def charisma(self, dipl_skill: int, cardinals_dict: Dict[str, Cardinal], threshold_modifier: int = 0) -> CheckResult:
        random_cardinals = random.sample(list(cardinals_dict.keys()), 2)
        belief = threshold_modifier

        for name in random_cardinals:
            belief += cardinals_dict[name].dipl_skill

        _print(loc.get("charisma_test", charisma=belief))

        _print(loc.get("test_input_3"))
        result1 = _roll_group(6, 1)

        _print(loc.get("test_input_4"))
        result2 = _roll_group(4, 2)

        player_score = dipl_skill + result1 + result2

        if player_score >= belief:
            return CheckResult.SUCCESS
        else:
            return CheckResult.FAILURE


skill_check = SkillCheckEngine()
