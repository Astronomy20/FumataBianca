# Playtest launchers

Scripts for trying out **a single part of the game** without having to
replay everything from the start each time. These are not automated tests
(those live in `tests/`, run with pytest) and they don't modify or
duplicate any game logic: each one builds a `Player` at the right rank and
calls the same entry-point function `main.py` would eventually reach.

## Usage

From the project root, or from inside this folder — both work:

```bash
python -m playtest.soldier
python -m playtest.priest
python -m playtest.bishop
python -m playtest.conclave
python -m playtest.credits
```

`playtest.credits` just shows the paginated end-of-game credits screen —
it doesn't need a Player at all.

## Customizing

Each script has a handful of constants at the top you can edit directly:

- `STAT_BOOST` — extra points added to every stat at character creation,
  useful for clearing the consensus thresholds (20 to become Bishop, 40 to
  become Cardinal) without having to grind choices beforehand. Set it to
  `0` for realistic day-one stats.
- `CITY` (`soldier.py` only) — forces the starting family/city to pick
  either the Florence/Savonarola branch or the Venice-Milan-Mantua one.

The generated stats are printed to the screen before the story starts, so
you always know what point you're starting from.
