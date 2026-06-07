import json
import os
import random
import sys
from typing import Dict, List

from models.domain import Cardinal, Family
from core.localization import resource_path


class FamilyRepository:
    def __init__(self) -> None:
        data_path = resource_path(os.path.join("data", "families.json"))
        with open(data_path, encoding="utf-8") as f:
            self._data = json.load(f)

    def get_random(self) -> Family:
        name, info = random.choice(list(self._data.items()))
        return Family(
            name=name,
            city=info["city"],
            context=info["context"],
            multipliers=info["multiplier"],
        )


class CardinalRepository:
    def __init__(self) -> None:
        data_path = resource_path(os.path.join("data", "cardinals.json"))
        with open(data_path, encoding="utf-8") as f:
            config = json.load(f)

        stat_min = config["stat_range"]["min"]
        stat_max = config["stat_range"]["max"]

        self._cardinals: Dict[str, Cardinal] = {
            name: Cardinal(
                name=name,
                voc=random.randint(stat_min, stat_max),
                pop_agr=random.randint(stat_min, stat_max),
                pol_infl=random.randint(stat_min, stat_max),
                cur_rel=random.randint(stat_min, stat_max),
                dipl_skill=random.randint(stat_min, stat_max),
            )
            for name in config["names"]
        }

    def get_all_dict(self) -> Dict[str, Cardinal]:
        return self._cardinals

    def get_random_sample(self, n: int) -> List[Cardinal]:
        return random.sample(list(self._cardinals.values()), n)


family_repo = FamilyRepository()
cardinal_repo = CardinalRepository()
