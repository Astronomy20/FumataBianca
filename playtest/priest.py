"""Playtest the Priest -> Parson storyline in isolation.

Not an automated test — run directly (either form works):
    python -m playtest.priest
    python playtest/priest.py
"""
import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _REPO_ROOT)
os.chdir(_REPO_ROOT)  # data/lang files are loaded relative to the cwd, like main.py expects

from models.domain import Rank
from playtest._common import setup, make_player

STAT_BOOST = 0  # priest.py checks consensus >= 20 to become Bishop at the end


def main() -> None:
    setup()
    player = make_player(rank=Rank.PRIEST, stat_boost=STAT_BOOST)

    from content.priest import run_why_priest
    run_why_priest(player)


if __name__ == "__main__":
    main()
