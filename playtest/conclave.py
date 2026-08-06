"""Playtest the Conclave — i.e. the Cardinal endgame — in isolation.

There's no separate Cardinal-only content in the game: becoming Cardinal
leads straight into the conclave, so this one launcher covers both.

Not an automated test — run directly (either form works):
    python -m playtest.conclave
    python playtest/conclave.py
"""
import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _REPO_ROOT)
os.chdir(_REPO_ROOT)  # data/lang files are loaded relative to the cwd, like main.py expects

from models.domain import Rank
from playtest._common import setup, make_player

STAT_BOOST = 10  # conclave skill checks are pitted against cardinal stats (5-10 each)


def main() -> None:
    setup()
    player = make_player(rank=Rank.CARDINAL, stat_boost=STAT_BOOST)

    from content.conclave import run_conclave_start
    run_conclave_start(player)


if __name__ == "__main__":
    main()
