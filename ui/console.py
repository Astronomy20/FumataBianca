import shutil
import sys
import textwrap
from core.localization import loc
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

    def gameover(self) -> None:
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
