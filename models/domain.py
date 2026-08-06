from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Tuple


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
    city: str  # canonical Italian city id, e.g. "Firenze" — used for game logic;
    # for display, localize it via loc.get(f"city_{city.lower()}")
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
    # The delta (already weighted by the family multiplier) from the last
    # add_points call, in order [voc, pop_agr, pol_infl, cur_rel, dipl_skill].
    # Used by the UI to show "+X"/"-X" next to stats that just changed.
    last_gain: Tuple[int, int, int, int, int] = field(default_factory=lambda: (0, 0, 0, 0, 0))

    @property
    def consensus(self) -> int:
        total = self.voc + self.pop_agr + self.pol_infl
        if self.rank in (Rank.BISHOP, Rank.CARDINAL):
            total += self.cur_rel + self.dipl_skill
        return total

    def add_points(
        self,
        voc: int = 0,
        pop_agr: int = 0,
        pol_infl: int = 0,
        cur_rel: int = 0,
        dipl_skill: int = 0,
    ) -> None:
        mult = self.family.multipliers
        weighted = (
            round(voc * mult[0]),
            round(pop_agr * mult[1]),
            round(pol_infl * mult[2]),
            round(cur_rel * mult[3]),
            round(dipl_skill * mult[4]),
        )

        self.voc += weighted[0]
        self.pop_agr += weighted[1]
        self.pol_infl += weighted[2]
        self.cur_rel += weighted[3]
        self.dipl_skill += weighted[4]

        self.last_gain = weighted
