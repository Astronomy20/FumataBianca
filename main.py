import json
import locale
import random

from core import loc, resource_path
from data.repositories import family_repo
from models import Player, Rank

_LANG_CODES = ["it", "en", "es", "fr", "de"]
_LOCALE_NORMALIZE = {
    "Italian": "it", "English": "en", "Spanish": "es", "French": "fr", "German": "de"
}


def _detect_default_lang() -> str:
    enc = locale.getlocale()
    if enc[1] == "1252":
        raw = (enc[0] or "en").split("_")[0]
        lang = _LOCALE_NORMALIZE.get(raw, "en")
    else:
        lang = (enc[0] or "en_US").split("_")[0]
    return lang if lang in _LANG_CODES else "en"


def _choose_language() -> str:
    def_lang = _detect_default_lang()
    loc.load(def_lang)

    with open(resource_path("lang/langs.json"), encoding="utf-8") as f:
        all_dicts = json.load(f)

    while True:
        print(loc.get("choose_lang"))
        lang_map = {str(i + 1): code for i, code in enumerate(_LANG_CODES)}
        for num, code in lang_map.items():
            print(f"{num} - {all_dicts.get(def_lang, {}).get(code, code)}")
        choice = input()
        if choice in lang_map:
            return lang_map[choice]
        print(loc.get("err"))


def _check_valid_name(prompt: str) -> str:
    raw = input(prompt)
    while True:
        if any(c.isalpha() for c in raw):
            return raw.capitalize()
        print(loc.get("name_err"))
        raw = input(loc.get("name"))


def _create_player(name: str) -> Player:
    family = family_repo.get_random()
    return Player(
        name=name,
        family=family,
        voc=round(random.randint(1, 5) * family.multipliers[0]) + random.randint(1, 5),
        pop_agr=round(random.randint(1, 5) * family.multipliers[1]) + random.randint(1, 5),
        pol_infl=round(random.randint(1, 5) * family.multipliers[2]) + random.randint(1, 5),
        cur_rel=round(random.randint(1, 5) * family.multipliers[3]) + random.randint(1, 5),
        dipl_skill=round(random.randint(1, 5) * family.multipliers[4]) + random.randint(1, 5),
    )


def main() -> None:
    lang = _choose_language()
    loc.load(lang)

    name = _check_valid_name(loc.get("name"))
    player = _create_player(name)

    from ui import ui

    ui.print_text(loc.get(
        "start",
        context=player.family.context,
        player_name=player.name,
        family_name=player.family.name,
        city=player.family.city,
    ))
    ui.go_on()

    while True:
        ui.print_text(loc.get("career_choice"))
        choice = input()

        if choice == "1":
            player.rank = Rank.PRIEST
            from content import run_why_priest
            run_why_priest(player)
            break
        elif choice == "2":
            player.rank = Rank.SOLDIER
            from content.soldier import run_firenze, run_venezia_milano_mantova
            if player.family.city == "Firenze":
                run_firenze(player)
            else:
                run_venezia_milano_mantova(player)
            break
        else:
            ui.error()


if __name__ == "__main__":
    main()
