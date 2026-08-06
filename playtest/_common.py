"""Shared setup for the manual playtest launchers in this folder.

These are NOT automated tests (see tests/ for those) and pytest will not
collect them. Each launcher just builds a Player at the rank you want to
try out and calls the same entry-point function main.py would eventually
reach — no game logic is duplicated or modified.

Run a launcher as a module from the repo root, e.g.:
    python -m playtest.bishop
"""
import random
from typing import Optional

from core import loc, terminal
from data.repositories import family_repo
from models.domain import Player, Rank


def setup(lang: str = "it") -> None:
    """Same startup main.py does: init the terminal, load the language."""
    terminal.init()
    loc.load(lang)


def make_player(
    name: str = "Playtest",
    rank: Rank = Rank.NOTHING,
    stat_boost: int = 0,
    city: Optional[str] = None,
) -> Player:
    """Build a Player using the same chargen formula as main.py's
    _create_player, optionally boosted so consensus thresholds don't
    require a full playthrough to reach, and optionally pinned to a
    specific family city (e.g. "Firenze") to force a particular branch.
    """
    family = family_repo.get_random()
    if city is not None:
        for _ in range(50):
            if family.city == city:
                break
            family = family_repo.get_random()

    def stat(index: int) -> int:
        return round(random.randint(1, 5) * family.multipliers[index]) + random.randint(1, 5) + stat_boost

    player = Player(
        name=name,
        family=family,
        voc=stat(0),
        pop_agr=stat(1),
        pol_infl=stat(2),
        cur_rel=stat(3),
        dipl_skill=stat(4),
        rank=rank,
    )

    print(f"--- Playtest: {player.name} of the {family.name} ({family.city}), rank={rank.name} ---")
    print(
        f"    voc={player.voc} pop_agr={player.pop_agr} pol_infl={player.pol_infl} "
        f"cur_rel={player.cur_rel} dipl_skill={player.dipl_skill}\n"
    )

    return player
