import shutil
import sys
import textwrap
from core.localization import loc, resource_path
from models.domain import Player


class ConsoleUI:
    def print_text(self, text: str) -> None:
        width = shutil.get_terminal_size().columns
        for paragraph in text.split("\n"):
            print(textwrap.fill(paragraph, width=width))

    def go_on(self) -> None:
        input(loc.get("go_on"))
        for _ in range(4):
            print("\033[1A\033[2K", end="")

    def error(self) -> None:
        print(loc.get("err"))

    def show_credits(self) -> None:
        input(loc.get("go_on"))
        print("\033[2J\033[H", end="")
        try:
            with open(resource_path("content/CREDITS.md"), encoding="utf-8") as f:
                print(f.read())
        except OSError:
            pass
        input(loc.get("credits_exit"))

    def gameover(self) -> None:
        self.show_credits()
        sys.exit()

    def print_points(self, player: Player) -> None:
        self.print_text(loc.get(
            "point_print",
            voc=player.voc,
            pop_agr=player.pop_agr,
            pol_infl=player.pol_infl,
            cur_rel=player.cur_rel,
            dipl_skills=player.dipl_skill,
            consensus=player.consensus,
        ))


ui = ConsoleUI()
