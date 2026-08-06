import random
import sys
import time
from typing import List, Optional, Tuple

from core import terminal
from core.localization import loc


COIN_FACES: List[List[str]] = [
    [
        " /‾‾‾‾‾\\ ",
        "|       |",
        "|   ☺   |",
        "|       |",
        " \\_____/ "
    ],
    [
        " /‾‾‾‾‾\\ ",
        "|       |",
        "|   €   |",
        "|       |",
        " \\_____/ "
    ]
]

D4_FACES: List[List[str]] = [
    [
        "    ▲    ",
        "  / 1 \\  ",
        " /_____\\ "
    ],
    [
        "    ▲    ",
        "  / 2 \\  ",
        " /_____\\ "
    ],
    [
        "    ▲    ",
        "  / 3 \\  ",
        " /_____\\ "
    ],
    [
        "    ▲    ",
        "  / 4 \\  ",
        " /_____\\ "
    ]
]

D6_FACES: List[List[str]] = [
    [
        "+---------+",
        "|         |",
        "|         |",
        "|    ●    |",
        "|         |",
        "|         |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●       |",
        "|         |",
        "|         |",
        "|         |",
        "|       ● |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●       |",
        "|         |",
        "|    ●    |",
        "|         |",
        "|       ● |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●     ● |",
        "|         |",
        "|         |",
        "|         |",
        "| ●     ● |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●     ● |",
        "|         |",
        "|    ●    |",
        "|         |",
        "| ●     ● |",
        "+---------+"
    ],
    [
        "+---------+",
        "| ●     ● |",
        "|         |",
        "| ●     ● |",
        "|         |",
        "| ●     ● |",
        "+---------+"
    ]
]


class DiceEngine:
    def roll(self, faces: int) -> int:
        return random.randint(1, faces)

    def _layout(self, faces: int) -> Optional[Tuple[List[List[str]], int]]:
        if faces == 2:
            return COIN_FACES, 5
        if faces == 4:
            return D4_FACES, 3
        if faces == 6:
            return D6_FACES, 7
        return None

    def _draw_row(self, faces_lines: List[List[str]], height: int) -> None:
        """Draw one or more dice side by side, one die per column."""
        up = terminal.move_up(height)
        start = "\r" if up else ""
        sys.stdout.write(up)
        gap = "   "
        for row in range(height):
            combined = gap.join(lines[row] for lines in faces_lines)
            sys.stdout.write(start + combined + " " * 10 + "\n")
        sys.stdout.flush()

    def animate_multiple(self, faces: int, count: int) -> None:
        """Same rolling animation as animate(), but for `count` dice of the
        same kind shown side by side at once."""
        layout = self._layout(faces)
        if layout is None:
            print(loc.get("err"))
            return

        # Without ANSI sequences the cursor can't move back up: no animation,
        # only the final face gets printed.
        if not terminal.ansi_enabled():
            return

        all_faces, height = layout
        duration = 1.5
        interval = 0.2
        end_time = time.time() + duration

        for _ in range(height):
            print()

        while time.time() < end_time:
            for face in all_faces:
                self._draw_row([face] * count, height)
                time.sleep(interval)

    def render_faces(self, faces: int, results: List[int]) -> None:
        """Draw the final, settled faces for several dice side by side,
        each showing its own correct result."""
        layout = self._layout(faces)
        if layout is None:
            print(loc.get("err"))
            return

        all_faces, height = layout
        self._draw_row([all_faces[r - 1] for r in results], height)

    def animate(self, faces: int) -> None:
        self.animate_multiple(faces, 1)

    def render_face(self, faces: int, result: int) -> None:
        self.render_faces(faces, [result])

    def face_coin(self, point_type: str) -> int:
        input(loc.get("coin_launch_input", point_type=point_type))

        self.animate(2)
        result = self.roll(2)

        self.render_face(2, result)

        if result == 1:
            print(loc.get("coin_output_heads", point_type=point_type))
            return 1
        else:
            print(loc.get("coin_output_tails", point_type=point_type))
            return -1

    def face_4(self, point_type: str, val: str) -> int:
        if val == "+":
            input(loc.get("dice_launch_input_pos", point_type=point_type))
        elif val == "-":
            input(loc.get("dice_launch_input_neg", point_type=point_type))
        else:
            print(loc.get("err"))

        self.animate(4)
        result = self.roll(4)

        self.render_face(4, result)

        if val == "+":
            if result == 1:
                print(loc.get("dice_output_pos_1", result=result, point_type=point_type))
            else:
                print(loc.get("dice_output_pos", result=result, point_type=point_type))
            return result
        elif val == "-":
            if result == 1:
                print(loc.get("dice_output_neg_1", result=result, point_type=point_type))
            else:
                print(loc.get("dice_output_neg", result=result, point_type=point_type))
            return -result
        else:
            print(loc.get("err"))
            return result

    def face_6(self, point_type: str, val: str) -> int:
        if val == "+":
            input(loc.get("dice_launch_input_pos", point_type=point_type))
        elif val == "-":
            input(loc.get("dice_launch_input_neg", point_type=point_type))
        else:
            print(loc.get("err"))

        self.animate(6)
        result = self.roll(6)

        self.render_face(6, result)

        if val == "+":
            if result == 1:
                print(loc.get("dice_output_pos_1", result=result, point_type=point_type))
            else:
                print(loc.get("dice_output_pos", result=result, point_type=point_type))
            return result
        elif val == "-":
            if result == 1:
                print(loc.get("dice_output_neg_1", result=result, point_type=point_type))
            else:
                print(loc.get("dice_output_neg", result=result, point_type=point_type))
            return -result
        else:
            print(loc.get("err"))
            return result


dice = DiceEngine()
