"""Playtest the Bishop storyline in isolation.

Not an automated test — run directly (either form works):
    python -m playtest.bishop
    python playtest/bishop.py
"""
import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _REPO_ROOT)
os.chdir(_REPO_ROOT)  # data/lang files are loaded relative to the cwd, like main.py expects

from models.domain import Rank
from playtest._common import setup, make_player

# bishop.py checks consensus >= 40 to become Cardinal at the end; bump this
# if you want a realistic shot at reaching it without grinding first.
STAT_BOOST = 5


def main() -> None:
    setup()
    player = make_player(rank=Rank.BISHOP, stat_boost=STAT_BOOST)

    from content.bishop import run_bishop
    run_bishop(player)


if __name__ == "__main__":
    main()
