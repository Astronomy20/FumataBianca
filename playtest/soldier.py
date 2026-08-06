"""Playtest the Soldier storyline in isolation.

Not an automated test — run directly (either form works):
    python -m playtest.soldier
    python playtest/soldier.py
"""
import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _REPO_ROOT)
os.chdir(_REPO_ROOT)  # data/lang files are loaded relative to the cwd, like main.py expects

from models.domain import Rank
from playtest._common import setup, make_player

STAT_BOOST = 0  # bump this if you want to breeze through the branch
CITY = None  # e.g. "Firenze" to force the Savonarola branch, None = random family


def main() -> None:
    setup()
    player = make_player(rank=Rank.SOLDIER, stat_boost=STAT_BOOST, city=CITY)

    if player.family.city == "Firenze":
        from content.soldier import run_firenze
        run_firenze(player)
    else:
        from content.soldier import run_venezia_milano_mantova
        run_venezia_milano_mantova(player)


if __name__ == "__main__":
    main()
