"""Playtest the end-of-game credits screen in isolation.

Not an automated test — run directly (either form works):
    python -m playtest.credits
    python playtest/credits.py
"""
import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _REPO_ROOT)
os.chdir(_REPO_ROOT)  # data/lang files are loaded relative to the cwd, like main.py expects

from playtest._common import setup
from ui import ui


def main() -> None:
    setup()
    ui.show_credits()


if __name__ == "__main__":
    main()
