from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List


class Rank(Enum):
    NOTHING = auto()
    SOLDIER = auto()
    PRIEST = auto()
    PARSON = auto()
    BISHOP = auto()
    CARDINAL = auto()


class Language(Enum):
    ITALIAN = "it"
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"


class CheckResult(Enum):
    SUCCESS = "+"
    FAILURE = "-"


@dataclass
class Family:
    name: str
    city: str
    context: str
    multipliers: List[float]  # [voc, pop_agr, pol_infl, cur_rel, dipl_skill]


@dataclass
class Cardinal:
    name: str
    voc: int
    pop_agr: int
    pol_infl: int
    cur_rel: int
    dipl_skill: int


@dataclass
class Player:
    name: str
    family: Family
    voc: int
    pop_agr: int
    pol_infl: int
    cur_rel: int
    dipl_skill: int
    rank: Rank = field(default_factory=lambda: Rank.NOTHING)

    @property
    def consensus(self) -> int:
        if self.rank in (Rank.BISHOP, Rank.CARDINAL):
            return round(
                (self.voc + self.pop_agr + self.pol_infl + self.cur_rel + self.dipl_skill)
                * self.family.multipliers[1]
            )
        return round((self.voc + self.pop_agr + self.pol_infl) * self.family.multipliers[1])

    def add_points(
        self,
        voc: int = 0,
        pop_agr: int = 0,
        pol_infl: int = 0,
        cur_rel: int = 0,
        dipl_skill: int = 0,
    ) -> None:
        self.voc += voc
        self.pop_agr += pop_agr
        self.pol_infl += pol_infl
        self.cur_rel += cur_rel
        self.dipl_skill += dipl_skill
