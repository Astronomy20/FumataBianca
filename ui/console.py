import shutil
import sys
import textwrap
from core import terminal
from core.localization import loc, resource_path
from models.domain import Family, Player, Rank


class ConsoleUI:
    def print_text(self, text: str) -> None:
        width = shutil.get_terminal_size().columns
        for paragraph in text.split("\n"):
            print(textwrap.fill(paragraph, width=width))

    def go_on(self) -> None:
        input(loc.get("go_on"))
        terminal.clear_lines(4)

    def error(self) -> None:
        print(loc.get("err"))

    CREDITS_WIDTH = 63

    def _center(self, text: str) -> str:
        columns = shutil.get_terminal_size().columns
        return "\n".join(
            line.center(columns) if line.strip() else line for line in text.split("\n")
        )

    def _credits_sections(self, text: str) -> list[str]:
        """Split CREDITS.md into its natural sections (bounded by the file's
        separator rules), with "Written By" further split into two roughly
        equal halves since it is by far the longest section."""
        lines = text.split("\n")
        separators = [
            i for i, line in enumerate(lines)
            if line.strip() and set(line.strip()) == {"─"}
        ]
        if len(separators) < 8:
            return [text]  # unexpected shape: fall back to a single section

        # TITLE, CREATED BY, HISTORICAL, STORY STRUCTURE, WRITTEN BY,
        # SPECIAL THANKS, LICENSE
        sections = [
            "\n".join(lines[a: b + 1]) for a, b in zip(separators, separators[1:])
        ]

        rule = "─" * self.CREDITS_WIDTH
        pad = [""] * 4  # the 4 blank lines every section opens with below its rule

        def entries(chunk: list[str]) -> list[str]:
            chunk = list(chunk)
            while chunk and chunk[-1] == "":
                chunk.pop()
            return chunk

        # "Written By" split into two roughly equal halves, each reading as
        # its own complete, independently centered section (same header,
        # symmetric padding around the entries).
        written = sections[4].split("\n")
        written_header = written[:8]  # rule, 4 blanks, "WRITTEN BY" header, 2 blanks
        priest_at = next(i for i, line in enumerate(written) if "Priest" in line)
        written_1 = "\n".join(written_header + entries(written[8:priest_at - 1]) + pad + [rule])
        written_2 = "\n".join(written_header + entries(written[priest_at:-1]) + pad + [rule])

        # "Special Thanks" split from the closing quote: the quote becomes
        # its own standalone framed page (no header, same symmetric padding).
        special = sections[5].split("\n")
        stars_first = next(i for i, line in enumerate(special) if line.strip().startswith("*"))
        stars_last = next(
            len(special) - 1 - i for i, line in enumerate(reversed(special))
            if line.strip().startswith("*")
        )
        thanks = "\n".join(special[:6] + entries(special[6:stars_first]) + pad + [rule])
        quote = "\n".join([rule] + pad + entries(special[stars_first:stars_last + 1]) + pad + [rule])

        return sections[:4] + [written_1, written_2, thanks, quote] + sections[6:]

    # Groups of consecutive sections (see `_credits_sections`) that form one
    # page each: title+created by, research+story structure, the two written
    # by halves, special thanks, the closing quote, license+closing.
    _CREDITS_PAGE_GROUPS = ((0, 2), (2, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9))

    def _credits_pages(self, sections: list[str]) -> list[str]:
        if len(sections) < self._CREDITS_PAGE_GROUPS[-1][1]:
            return sections  # already a single fallback section

        rule = "─" * self.CREDITS_WIDTH
        pages = []
        for a, b in self._CREDITS_PAGE_GROUPS:
            merged = sections[a].split("\n")
            for section in sections[a + 1: b]:
                lines = section.split("\n")
                if lines and lines[0] == rule:
                    lines = lines[1:]  # already the previous section's closing rule
                merged += lines
            pages.append("\n".join(merged))
        return pages

    def _center_block(self, block: str, reserve_bottom: int) -> str:
        """Center `block` horizontally, as a fixed-width unit matching the
        manual centering already baked into CREDITS.md, and vertically
        within the terminal, leaving `reserve_bottom` rows for the prompt."""
        columns, height = shutil.get_terminal_size()
        margin = " " * max((columns - self.CREDITS_WIDTH) // 2, 0)
        lines = [margin + line for line in block.split("\n")]
        top_pad = max((height - reserve_bottom - len(lines)) // 2, 0)
        return "\n".join([""] * top_pad + lines)

    def show_credits(self) -> None:
        input(loc.get("go_on"))
        try:
            with open(resource_path("content/CREDITS.md"), encoding="utf-8") as f:
                text = f.read()
        except OSError:
            text = ""

        # Reserve exactly as many rows as the prompts actually print, so the
        # block ends up genuinely centered instead of drifting upward.
        go_on_rows = len(loc.get("go_on").split("\n"))
        exit_rows = len(loc.get("credits_exit").split("\n"))

        height = shutil.get_terminal_size().lines
        if text.count("\n") + 1 <= height - exit_rows:
            # Fits in one screen: no need to split into sections at all.
            terminal.clear_screen()
            print(self._center_block(text, reserve_bottom=exit_rows))
            input(self._center(loc.get("credits_exit")))
            return

        pages = self._credits_pages(self._credits_sections(text))
        for i, page in enumerate(pages):
            terminal.clear_screen()
            reserve = go_on_rows if i < len(pages) - 1 else exit_rows
            print(self._center_block(page, reserve_bottom=reserve))
            if i < len(pages) - 1:
                input(self._center(loc.get("go_on")))

        input(self._center(loc.get("credits_exit")))

    def gameover(self) -> None:
        self.show_credits()
        sys.exit()

    _GLI_PREFIXES = ("gn", "ps", "pn", "x", "y", "z")
    _VOWELS = "aeiouAEIOU"

    def _italian_plural_article(self, name: str) -> str:
        """"gli" before a vowel, "s" + consonant, or gn/ps/pn/x/y/z; "i" otherwise."""
        if not name or name[0] in self._VOWELS:
            return "gli"
        lowered = name.lower()
        if lowered.startswith(self._GLI_PREFIXES):
            return "gli"
        if lowered[0] == "s" and len(lowered) > 1 and lowered[1] not in "aeiou":
            return "gli"
        return "i"

    def _with_delta(self, value: int, delta: int) -> str:
        if delta > 0:
            return f"{value} (+{delta})"
        if delta < 0:
            return f"{value} ({delta})"
        return str(value)

    def print_points(self, player: Player) -> None:
        voc_gain, pop_agr_gain, pol_infl_gain, cur_rel_gain, dipl_skill_gain = player.last_gain
        mult = player.family.multipliers

        included_keys = ["stat_name_voc", "stat_name_pop_agr", "stat_name_pol_infl"]
        consensus_gain = voc_gain + pop_agr_gain + pol_infl_gain
        counts_everything = player.rank in (Rank.BISHOP, Rank.CARDINAL)
        if counts_everything:
            included_keys += ["stat_name_cur_rel", "stat_name_dipl_skill"]
            consensus_gain += cur_rel_gain + dipl_skill_gain

        consensus_scope = (
            loc.get("consensus_scope_all") if counts_everything
            else " + ".join(loc.get(key) for key in included_keys)
        )

        self.print_text(loc.get(
            "point_print",
            voc_mult=mult[0],
            pop_agr_mult=mult[1],
            pol_infl_mult=mult[2],
            cur_rel_mult=mult[3],
            dipl_skill_mult=mult[4],
            voc=self._with_delta(player.voc, voc_gain),
            pop_agr=self._with_delta(player.pop_agr, pop_agr_gain),
            pol_infl=self._with_delta(player.pol_infl, pol_infl_gain),
            cur_rel=self._with_delta(player.cur_rel, cur_rel_gain),
            dipl_skills=self._with_delta(player.dipl_skill, dipl_skill_gain),
            consensus_scope=consensus_scope,
            consensus=self._with_delta(player.consensus, consensus_gain),
        ))

    def print_family_multipliers(self, family: Family) -> None:
        mult = family.multipliers
        self.print_text(loc.get(
            "family_multipliers_intro",
            family_article=self._italian_plural_article(family.name),
            family_name=family.name,
            voc_mult=mult[0],
            pop_agr_mult=mult[1],
            pol_infl_mult=mult[2],
            cur_rel_mult=mult[3],
            dipl_skill_mult=mult[4],
        ))


ui = ConsoleUI()
