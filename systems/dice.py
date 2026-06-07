import random
import sys
import time
from typing import List

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

    def animate(self, faces: int) -> None:
        duration = 1.5
        interval = 0.2
        end_time = time.time() + duration

        if faces == 2:
            for _ in range(5):
                print()

            while time.time() < end_time:
                for face in COIN_FACES:
                    sys.stdout.write("\033[5A")
                    for line in face:
                        sys.stdout.write("\r" + line + " " * 10 + "\n")
                    sys.stdout.flush()
                    time.sleep(interval)

        elif faces == 4:
            for _ in range(3):
                print()

            while time.time() < end_time:
                for face in D4_FACES:
                    sys.stdout.write("\033[3A")
                    for line in face:
                        sys.stdout.write("\r" + line + " " * 10 + "\n")
                    sys.stdout.flush()
                    time.sleep(interval)

        elif faces == 6:
            for _ in range(7):
                print()

            while time.time() < end_time:
                for face in D6_FACES:
                    sys.stdout.write("\033[7A")
                    for line in face:
                        sys.stdout.write("\r" + line + " " * 10 + "\n")
                    sys.stdout.flush()
                    time.sleep(interval)
        else:
            print(loc.get("err"))

    def render_face(self, faces: int, result: int) -> None:
        if faces == 2:
            returns = 5
            ascii_lines = COIN_FACES[result - 1]
        elif faces == 4:
            returns = 3
            ascii_lines = D4_FACES[result - 1]
        elif faces == 6:
            returns = 7
            ascii_lines = D6_FACES[result - 1]
        else:
            print(loc.get("err"))
            return

        sys.stdout.write(f"\033[{returns}A")
        for line in ascii_lines:
            sys.stdout.write("\r" + line + " " * 10 + "\n")
        sys.stdout.flush()

    def face_coin(self, point_type: str) -> int:
        input(loc.get("coin_launch_input", point_type=point_type))

        self.animate(2)
        result = self.roll(2)

        self.render_face(2, result)

        if result == 1:
            print(loc.get("coin_output_heads", point_type=point_type))
        else:
            print(loc.get("coin_output_tails", point_type=point_type))

        return result

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
        elif val == "-":
            if result == 1:
                print(loc.get("dice_output_neg_1", result=result, point_type=point_type))
            else:
                print(loc.get("dice_output_neg", result=result, point_type=point_type))
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
        elif val == "-":
            if result == 1:
                print(loc.get("dice_output_neg_1", result=result, point_type=point_type))
            else:
                print(loc.get("dice_output_neg", result=result, point_type=point_type))
        else:
            print(loc.get("err"))

        return result


dice = DiceEngine()
