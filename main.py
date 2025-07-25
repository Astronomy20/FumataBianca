import locale
import json
import random
import time
import os
import sys
import shutil
import textwrap


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



class Dialogs:
    normalize_encode = {
        "Italian": "it",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de"
    }

    available_langs = {
        "it": "Italian",
        "en": "English",
        "es": "Spanish",
        "fr": "French",
        "de": "German"
    }

    @staticmethod
    def choose_language():
        with open(resource_path("lang/langs.json")) as f:
            all_dicts = json.load(f)

        locale_encoding = locale.getlocale()

        if locale_encoding[1] == "1252":
            def_lang = Dialogs.normalize_encode.get(locale_encoding[0].split('_')[0])

            if def_lang in Dialogs.available_langs:
                pass
            else:
                def_lang = "en"
        else:
            def_lang = locale_encoding[0].split('_')[0]
            if def_lang in Dialogs.available_langs:
                pass
            else:
                def_lang = "en"

        while True:
            print(Dialogs.load_dialogs(def_lang)["choose_lang"])

            i = 0
            lang_map = {}
            for _ in Dialogs.normalize_encode.values():
                i += 1
                lang_map[str(i)] = _
                print(f"{i} - {all_dicts[def_lang][_]}")

            lang = input()

            if lang in lang_map:
                return lang_map[lang]
            else:
                print(Dialogs.load_dialogs(def_lang)["err"])

    @staticmethod
    def load_dialogs(lang):
        with open(resource_path(f'lang/{lang}.json'), 'r', encoding='utf_8') as lang:
            dialogs = json.load(lang)

        return dialogs


choose_lang = Dialogs.choose_language()


class Utility:
    @staticmethod
    def error():
        print(Dialogs.load_dialogs(choose_lang)["err"])

    @staticmethod
    def check_valid_name(input_name):
        check_username = input_name
        while True:
            if any(char.isalpha() for char in check_username):
                username = check_username.capitalize()
                break
            else:
                print(Dialogs.load_dialogs(choose_lang)["name_err"])
                check_username = input(Dialogs.load_dialogs(choose_lang)["name"])

        return username

    @staticmethod
    def go_on():
        input(Dialogs.load_dialogs(choose_lang)["go_on"])

        for _ in range(4):
            print("\033[1A\033[2K", end="")

    @staticmethod
    def fixed_print(text):
        width = shutil.get_terminal_size().columns
        for paragraph in text.split("\n"):
            formatted_text = textwrap.fill(paragraph, width=width)
            print(formatted_text)

    @staticmethod
    def timeout():
        time.sleep(5)

    @staticmethod
    def print_points(player):
        print(Dialogs.load_dialogs(choose_lang)["point_print"].format(
            voc=player.voc,
            pop_agr=player.pop_agr,
            pol_infl=player.pol_infl,
            cur_rel=player.cur_rel,
            dipl_skills=player.dipl_skill,
            consensus=player.consensus
        ))

    @staticmethod
    def gameover():
        sys.exit()


coin = [
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

d4_faces = [
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

d6_faces = [
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


class Dices:
    @staticmethod
    def roll_dice(faces_num):
        return random.randint(1, faces_num)

    @staticmethod
    def roll_animation(faces):
        duration = 1.5
        interval = 0.2
        end_time = time.time() + duration

        if faces == 2:
            for _ in range(5):
                print()

            while time.time() < end_time:
                for face in coin:
                    sys.stdout.write("\033[5A")
                    for line in face:
                        sys.stdout.write("\r" + line + " " * 10 + "\n")
                    sys.stdout.flush()
                    time.sleep(interval)

        elif faces == 4:
            for _ in range(3):
                print()

            while time.time() < end_time:
                for face in d4_faces:
                    sys.stdout.write("\033[3A")  # Move cursor up 3 lines
                    for line in face:
                        sys.stdout.write("\r" + line + " " * 10 + "\n")
                    sys.stdout.flush()
                    time.sleep(interval)
        elif faces == 6:
            for _ in range(7):
                print()

            while time.time() < end_time:
                for face in d6_faces:
                    sys.stdout.write("\033[7A")
                    for line in face:
                        sys.stdout.write("\r" + line + " " * 10 + "\n")
                    sys.stdout.flush()
                    time.sleep(interval)
        else:
            Utility.error()

    @staticmethod
    def print_final_face(ascii_lines, faces):
        returns = 0

        if faces == 2:
            returns = 5
        elif faces == 4:
            returns = 3
        elif faces == 6:
            returns = 7
        else:
            Utility.error()

        sys.stdout.write(f"\033[{returns}A")
        for line in ascii_lines:
            sys.stdout.write("\r" + line + " " * 10 + "\n")
        sys.stdout.flush()

    @staticmethod
    def face_2(point_type):
        input(Dialogs.load_dialogs(Game.lang)["coin_launch_input"].format(
            point_type=point_type
        ))

        Dices.roll_animation(2)
        result = Dices.roll_dice(2)

        Dices.print_final_face(coin[result - 1], 2)

        if result == 1:
            print(Dialogs.load_dialogs(Game.lang)["coin_output_heads"].format(
                point_type=point_type
            ))

        else:
            print(Dialogs.load_dialogs(Game.lang)["coin_output_tails"].format(
                point_type=point_type
            ))

        return result

    @staticmethod
    def face_4(point_type, val):
        if val == "+":
            input(Dialogs.load_dialogs(Game.lang)["dice_launch_input_pos"].format(
                point_type=point_type
            ))
        elif val == "-":
            input(Dialogs.load_dialogs(Game.lang)["dice_launch_input_neg"].format(
                point_type=point_type
            ))
        else:
            Utility.error()

        Dices.roll_animation(4)
        result = Dices.roll_dice(4)

        Dices.print_final_face(d4_faces[result - 1], 4)

        if val == "+":
            if result == 1:
                print(Dialogs.load_dialogs(Game.lang)["dice_output_pos_1"].format(
                    result=result,
                    point_type=point_type
                ))
            else:
                print(Dialogs.load_dialogs(Game.lang)["dice_output_pos"].format(
                    result=result,
                    point_type=point_type
                ))
        elif val == "-":
            if result == 1:
                print(Dialogs.load_dialogs(Game.lang)["dice_output_neg_1"].format(
                    result=result,
                    point_type=point_type
                ))
            else:
                print(Dialogs.load_dialogs(Game.lang)["dice_output_neg"].format(
                    result=result,
                    point_type=point_type
                ))
        else:
            Utility.error()

        return result

    @staticmethod
    def face_6(point_type, val):
        if val == "+":
            input(Dialogs.load_dialogs(Game.lang)["dice_launch_input_pos"].format(
                point_type=point_type
            ))
        elif val == "-":
            input(Dialogs.load_dialogs(Game.lang)["dice_launch_input_neg"].format(
                point_type=point_type
            ))
        else:
            Utility.error()

        Dices.roll_animation(6)
        result = Dices.roll_dice(6)

        Dices.print_final_face(d6_faces[result - 1], 6)

        if val == "+":
            if result == 1:
                print(Dialogs.load_dialogs(Game.lang)["dice_output_pos_1"].format(
                    result=result,
                    point_type=point_type
                ))
            else:
                print(Dialogs.load_dialogs(Game.lang)["dice_output_pos"].format(
                    result=result,
                    point_type=point_type
                ))
        elif val == "-":
            if result == 1:
                print(Dialogs.load_dialogs(Game.lang)["dice_output_neg_1"].format(
                    result=result,
                    point_type=point_type
                ))
            else:
                print(Dialogs.load_dialogs(Game.lang)["dice_output_neg"].format(
                    result=result,
                    point_type=point_type
                ))
        else:
            Utility.error()

        return result


class Test:
    @staticmethod
    def faith(voc):
        random_cardinals = random.sample(list(cardinals.keys()), random.randint(2, 3))
        belief = 0

        for name in random_cardinals:
            belief += cardinals[name][0]

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["faith_test"].format(
            faith=belief
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_1"])
        input()
        Dices.roll_dice(6)
        result1 = Dices.roll_dice(6)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result1*2
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_2"])
        input()
        Dices.roll_dice(4)
        result2 = Dices.roll_dice(4)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result2*3
        ))

        player_score = voc + result1 * 2 + result2 * 3

        if player_score >= belief:
            return "+"
        else:
            return "-"

    @staticmethod
    def secrets():
        random_value = random.randint(10, 15)

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["secrets_test"].format(
            secrets=random_value
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_3"])
        input()
        Dices.roll_dice(6)
        result1 = Dices.roll_dice(6)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result1
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_4"])
        input()
        Dices.roll_dice(4)
        result2 = Dices.roll_dice(4)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result2*2
        ))

        player_score = result1 + result2 * 2

        if player_score >= random_value:
            return "+"
        else:
            return "-"

    @staticmethod
    def inlfuence(influence):
        random_cardinals = random.sample(list(cardinals.keys()), random.randint(2, 3))
        belief = 0

        for name in random_cardinals:
            belief += cardinals[name][1]

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["influence_test"].format(
            belief=belief
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_1"])
        input()
        Dices.roll_dice(6)
        result1 = Dices.roll_dice(6)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result1*2
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_2"])
        input()
        Dices.roll_dice(4)
        result2 = Dices.roll_dice(4)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result2*3
        ))

        player_score = influence + result1 * 2 + result2 * 3

        if player_score >= belief:
            return "+"
        else:
            return "-"

    @staticmethod
    def strategy():
        random_value = random.randint(10, 20)

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["strategy_test"].format(
            strategy=random_value
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_1"])
        input()
        Dices.roll_dice(6)
        result1 = Dices.roll_dice(6)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result1*2
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_2"])
        input()
        Dices.roll_dice(4)
        result2 = Dices.roll_dice(4)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result2*3
        ))

        player_score = result1 * 2 + result2 * 3

        if player_score >= random_value:
            return "+"
        else:
            return "-"

    @staticmethod
    def charisma(dipl_skill):
        random_cardinals = random.sample(list(cardinals.keys()), 2)
        belief = 0

        for name in random_cardinals:
            belief += cardinals[name][4]

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["charisma_test"].format(
            charisma=belief
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_3"])
        input()
        Dices.roll_dice(6)
        result1 = Dices.roll_dice(6)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result1*1
        ))

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_input_4"])
        input()
        Dices.roll_dice(4)
        result2 = Dices.roll_dice(4)
        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["test_result"].format(
            result=result2*2
        ))

        player_score = dipl_skill + result1 * 2 + result2 * 3

        if player_score >= belief:
            return "+"
        else:
            return "-"


class CardinalsValues:
    @staticmethod
    def voc():
        return random.randint(5, 10)

    @staticmethod
    def pop_agr():
        return random.randint(5, 10)

    @staticmethod
    def pol_infl():
        return random.randint(5, 10)

    @staticmethod
    def cur_rel():
        return random.randint(5, 10)

    @staticmethod
    def dipl_skill():
        return random.randint(5, 10)


cardinals = {
    "Giovanni de' Medici": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                            CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Bernardino López de Carvajal": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Francesco Alidosi": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                          CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Marco Cornaro": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                      CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Bandinello Sauli": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                         CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Francesco Soderini": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                           CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Alessandro Farnese": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                           CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Antonio Maria Ciocchi del Monte": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                        CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Raffaele Riario": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                        CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Leonardo Grosso della Rovere": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Gabriele de' Gabrielli": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                               CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Giovanni Battista Pallavicino": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                      CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Lorenzo Pucci": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                      CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Giulio de' Medici": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                          CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Matthäus Schiner": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                         CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Tamás Bakócz": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "René de Prie": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Robert Guibé": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                     CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Georges d'Amboise": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                          CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Jean-François de la Trémoille": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                      CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Luis de Borja-Lanzol": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                             CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Juan Castellar y de Borja": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                  CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Guillaume Briçonnet": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                            CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Pierre d'Ailly": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                       CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Jean de La Palud": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                         CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Fazio Giovanni Santori": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                               CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Galeotto Franciotti della Rovere": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                                         CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Niccolò Fieschi": [CardinalsValues.voc(), CardinalsValues.pop_agr(), CardinalsValues.pol_infl(),
                        CardinalsValues.cur_rel(), CardinalsValues.dipl_skill()],
    "Francesco Armellini Pantalassi de' Medici": [CardinalsValues.voc(), CardinalsValues.pop_agr(),
                                                  CardinalsValues.pol_infl(), CardinalsValues.cur_rel(),
                                                  CardinalsValues.dipl_skill()]
}

families_data = {
    "Gonzaga": {
        "multiplier": [1, 1.1, 1.3, 0.8, 1.2],
        "context": "Milano sotto gli Sforza, Firenze sotto i Medici, la Repubblica di Venezia e la tua Mantova "
                   "sotto il controllo gonzaghese",
        "city": "Mantova"
    },
    "Orseolo": {
        "multiplier": [1, 1.4, 1.2, 0.75, 1.5],
        "context": "Milano sotto gli Sforza, Mantova sotto i Gonzaga, Firenze e la tua Repubblica di Venezia",
        "city": "Venezia"
    },
    "Scotti": {
        "multiplier": [1.1, 1, 1.4, 1, 1.1],
        "context": "Firenze sotto i Medici, Mantova sotto i Gonzaga, la Repubblica di Venezia e la tua Milano sotto "
                   "il controllo sforzesco",
        "city": "Milano"
    },
    "Strozzi": {
        "multiplier": [1, 0.85, 1.3, 1.1, 1],
        "context": "Milano sotto gli Sforza, Mantova sotto i Gonzaga, la Repubblica di Venezia e la tua Firenze "
                   "sotto il controllo mediceo",
        "city": "Firenze"
    }
}


class Families:
    def __init__(self):
        self.fam_name = ""
        self.fam_city = ""
        self.fam_context = ""
        self.fam_multipliers = []
        self.voc = 0
        self.pop_agr = 0
        self.pol_infl = 0
        self.cur_rel = 0
        self.dipl_skill = 0

    def family(self):
        self.fam_name, info = random.choice(list(families_data.items()))
        self.fam_multipliers = info["multiplier"]
        self.fam_city = info["city"]
        self.fam_context = info["context"]
        self.voc, self.pop_agr, self.pol_infl, self.cur_rel, self.dipl_skill = self.fam_multipliers
        return self.fam_name, self.fam_city, self.fam_context, self.fam_multipliers

    def print_stats(self):
        print(f'Famiglia: {self.fam_name} di {self.fam_city}'
              '\n')
        print(f'Moltiplicatori della famiglia di {self.fam_name}:'
              f'\nVocazione: {self.voc}'
              f'\nConsenso popolare: {self.pop_agr}'
              f'\nInfluenza politica: {self.pol_infl}'
              f'\nRilevanza curiale: {self.cur_rel}'
              f'\nAbilità diplomatica: {self.dipl_skill}'
              '\n')
        print(f'Contesto: {self.fam_context}')


class PlayerValues:
    @staticmethod
    def voc():
        return random.randint(1, 5)

    @staticmethod
    def pop_agr():
        return random.randint(1, 5)

    @staticmethod
    def pol_infl():
        return random.randint(1, 5)

    @staticmethod
    def cur_rel():
        return random.randint(1, 5)

    @staticmethod
    def dipl_skill():
        return random.randint(1, 5)


class Player:
    def __init__(self, name, voc, pop_agr, pol_infl, cur_rel, dipl_skill):
        # Player Name
        self.player_name = name

        # Family assignment
        self.fam = Families()
        self.fam_name, self.fam_city, self.fam_context, self.fam_val = self.fam.family()

        # Family Multipliers
        self.fam_voc = self.fam_val[0]
        self.fam_pop_agr = self.fam_val[1]
        self.fam_pol_infl = self.fam_val[2]
        self.fam_cur_rel = self.fam_val[3]
        self.fam_dipl_skill = self.fam_val[4]

        # Player Attributes
        self.voc = round(random.randint(1, 5) * self.fam_voc) + voc
        self.pop_agr = round(random.randint(1, 5) * self.fam_pop_agr) + pop_agr
        self.pol_infl = round(random.randint(1, 5) * self.fam_pol_infl) + pol_infl
        self.cur_rel = round(random.randint(1, 5) * self.fam_cur_rel) + cur_rel
        self.dipl_skill = round(random.randint(1, 5) * self.fam_dipl_skill) + dipl_skill

        self.player_values = [self.voc, self.pop_agr, self.pol_infl, self.cur_rel, self.dipl_skill]

        # Status
        self.isnothing = True
        self.issoldier = False
        self.ispriest = False
        self.isparson = False
        self.isbishop = False
        self.iscardinal = False

        # Calculation of consensus
        if self.isbishop or self.iscardinal:
            self.consensus = round(
                (self.voc + self.pop_agr + self.pol_infl + self.cur_rel + self.dipl_skill) * self.fam_val[1])
        else:
            self.consensus = round(
                (self.voc + self.pop_agr + self.pol_infl) * self.fam_val[1])

    def add_points(self, voc, pop_agr, pol_infl, cur_rel, dipl_skill):
        self.voc += voc
        self.pop_agr += pop_agr
        self.pol_infl += pol_infl
        self.cur_rel += cur_rel
        self.dipl_skill += dipl_skill

        # Calculation of new consensus
        if self.isbishop or self.iscardinal:
            self.consensus = round(
                (self.voc + self.pop_agr + self.pol_infl + self.cur_rel + self.dipl_skill) * self.fam_val[1])
        else:
            self.consensus = round(
                (self.voc + self.pop_agr + self.pol_infl) * self.fam_val[1])


class Game:
    lang = choose_lang
    username = Utility.check_valid_name(input(Dialogs.load_dialogs(lang)["name"]))

    dice_voc = Dialogs.load_dialogs(lang)["dice_voc"]
    dice_pop_agr = Dialogs.load_dialogs(lang)["dice_pop_agr"]
    dice_pol_infl = Dialogs.load_dialogs(lang)["dice_pol_infl"]
    dice_cur_rel = Dialogs.load_dialogs(lang)["dice_cur_rel"]
    dice_dipl_skill = Dialogs.load_dialogs(lang)["dice_dipl_skills"]

    def __init__(self):
        self.player = Player(Game.username, PlayerValues.voc(), PlayerValues.pop_agr(), PlayerValues.pol_infl(),
                             PlayerValues.cur_rel(), PlayerValues.dipl_skill())

    def start(self):
        player_name = self.player.player_name

        family_name = self.player.fam_name
        city = self.player.fam_city
        context = self.player.fam_context

        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["start"].format(
            context=context,
            player_name=player_name,
            family_name=family_name,
            city=city
        ))

        Utility.go_on()

        while True:
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["career_choice"])
            choice = input()

            if choice == "1":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["priest"])
                self.player.ispriest = True
                self.player.isnothing = False

                Game.Priest(self.player).why_priest()
                break
            elif choice == "2":
                self.player.issoldier = True
                self.player.isnothing = False

                if city == "Firenze":
                    Game.Soldier(self.player).firenze()

                elif city == "Milano" or "Mantova" or "Venezia":
                    Game.Soldier(self.player).venezia_milano_mantova()

                else:
                    Utility.error()

                break
            else:
                Utility.error()

    class Soldier:
        def __init__(self, player):
            self.player = player

        def firenze(self):
            self.player.issoldier = True

            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["firenze_init"])

                Utility.go_on()

                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["firenze_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["firenze_1"])

                    Player.add_points(self.player, Dices.face_4(Game.dice_voc, "+"), 0, 0, 0, 0)
                    Utility.print_points(self.player)

                    self.player.issoldier = False
                    self.player.ispriest = True

                    Utility.go_on()

                    Game.Priest(self.player).sermon()

                    break
                elif choice == "2":
                    prob = random.randint(1, 100)
                    if prob <= 95:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["firenze_2_pos"])

                        Player.add_points(self.player, Dices.face_4(Game.dice_voc, "+"), 0, 0, 0, 0)
                        Utility.print_points(self.player)
                        self.player.issoldier = False
                        self.player.ispriest = True

                        Utility.go_on()

                        Game.Priest(self.player).sermon()
                    elif prob > 95:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["firenze_2_neg"])

                        Utility.gameover()
                    else:
                        Utility.error()
                    break
                else:
                    Utility.error()

        def venezia_milano_mantova(self):
            self.player.issoldier = True

            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["ven_mil_mant_input"].format(
                    fam_city=self.player.fam_city
                ))
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["ven_mil_mant_1_pos"])

                    prob = random.randint(1, 100)

                    if prob <= 85:
                        self.player.issoldier = False
                        self.player.ispriest = True

                        Player.add_points(self.player, Dices.face_4(Game.dice_voc, "+"), 0, 0, 0, 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        Game.Priest(self.player).sermon()
                        break
                    elif prob > 85:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["ven_mil_mant_1_neg"])

                        Utility.gameover()
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["ven_mil_mant_2"])

                    self.player.issoldier = False
                    self.player.ispriest = True

                    Player.add_points(self.player, Dices.face_2(Game.dice_voc), 0, 0, 0, 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    Game.Priest(self.player).sermon()
                    break
                else:
                    Utility.error()

    class Priest:
        def __init__(self, player):
            self.player = player

        def why_priest(self):
            self.player.ispriest = True

            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["why_priest_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["why_priest_1"])

                    Player.add_points(self.player, Dices.face_4(Game.dice_voc, "+"), 0, 0, 0, 0)
                    Utility.print_points(self.player)

                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["why_priest_2"])

                    break
                else:
                    Utility.error()

            Utility.go_on()
            self.sermon()

        def sermon(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["sermon_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["sermon_1"])

                    Player.add_points(self.player, 2, Dices.face_4(Game.dice_pop_agr, "+"), 0, 0, 0)
                    Utility.print_points(self.player)

                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["sermon_2"])

                    Player.add_points(self.player, 0, 1, Dices.face_4(Game.dice_pol_infl, "-"), 0, 0)
                    Utility.print_points(self.player)

                    break
                else:
                    Utility.error()

            Utility.go_on()
            self.present()

        def present(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["present_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["present_1"])

                    Player.add_points(self.player, 1, 2, 0, 0, 0)
                    Utility.print_points(self.player)

                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["present_2"])

                    Utility.gameover()

                    break
                elif choice == "3":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["present_3"])

                    Player.add_points(self.player, 0, 0, (-1), 0, 0)
                    Utility.print_points(self.player)

                    break
                else:
                    Utility.error()

            Utility.go_on()
            self.become_parson()

        def become_parson(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["become_parson_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["become_parson_1"])

                    Player.add_points(self.player, 0, Dices.face_4(Game.dice_pop_agr, "+"),
                                      Dices.face_4(Game.dice_pol_infl, "+"), 0, 0)
                    Utility.print_points(self.player)
                    self.player.isparson = True

                    Utility.go_on()

                    self.cardinal_letter()
                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["become_parson_2"])

                    Player.add_points(self.player, 0, 1, 0, 0, 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    self.annul_marriage()
                    break
                else:
                    Utility.error()

        def cardinal_letter(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["cardinal_letter_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["cardinal_letter_1"])

                    Player.add_points(self.player, Dices.face_2(Game.dice_voc), 0, 2, 2, 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    self.annul_marriage()
                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["cardinal_letter_2"])

                    Player.add_points(self.player, 0, 0, 0, 1, 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    self.annul_marriage()
                    break
                elif choice == "3":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["cardinal_letter_3"])

                    Utility.go_on()

                    self.annul_marriage()
                    break
                else:
                    Utility.error()

        def annul_marriage(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["annul_marriage_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["annul_marriage_1"])

                    Utility.gameover()

                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["annul_marriage_2_pos"])

                    Player.add_points(self.player, (-2), 0, 2, 0, 0)
                    Utility.print_points(self.player)

                    if not self.player.isparson:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["annul_marriage_2_neg"])

                        Utility.gameover()
                    else:
                        Utility.go_on()

                        self.try_become_bishop()
                    break
                elif choice == "3":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["annul_marriage_3_pos"])

                    Player.add_points(self.player, (-2), 0, 1, 0, 0)
                    Utility.print_points(self.player)

                    if not self.player.isparson:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["annul_marriage_3_neg"])

                        Utility.gameover()
                    else:

                        Utility.go_on()

                        self.try_become_bishop()
                    break
                elif choice == "4":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["annul_marriage_4"])

                    Player.add_points(self.player, 1, 0, (-3), 0, 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    self.try_become_bishop()
                    break
                else:
                    Utility.error()

        def try_become_bishop(self):
            if self.player.consensus >= 20:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["become_bishop_pos"])

                self.player.ispriest = False
                self.player.isparson = False
                self.player.isbishop = True

                Utility.go_on()

                Game.Bishop(self.player).residence()
            elif self.player.consensus < 20:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["become_bishop_neg"])

                Utility.gameover()
            else:
                Utility.error()

    class Bishop:
        def __init__(self, player):
            self.player = player
            self.was_neutral = False
            self.was_france_ambassador = False
            self.was_sri_strong = False
            self.was_sri_calm = False
            self.was_opposer = False
            self.battle_neutral = False
            self.battle_injured = False

        def residence(self):
            self.player.ispriest = False
            self.player.isbishop = True

            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["residence_input"].format(
                    fam_city=self.player.fam_city
                ))
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["residence_1"])

                    Player.add_points(self.player, 2, 0, 0, 0, 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    self.taxation()
                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["residence_2"])

                    Player.add_points(self.player, 0, (-2), 0, 3, 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    self.help_cardinal()
                    break
                else:
                    Utility.error()

        def taxation(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["taxation_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["taxation_1"])

                    Player.add_points(self.player, 0, (-2), 2, 1, 1)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["taxation_2"])

                    Player.add_points(self.player, 0, 2, (-1), (-1), 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    break
                else:
                    Utility.error()

            self.lega_cambrai()

        def help_cardinal(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["help_cardinal_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["help_cardinal_1"])

                    Player.add_points(self.player, 0, (-1), Dices.face_2(Game.dice_pol_infl), 1, 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["help_cardinal_2"])

                    Player.add_points(self.player, Dices.face_4(Game.dice_voc, "+"), 1, 0, (-2), 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    break
                else:
                    Utility.error()

            self.lega_cambrai()

        def lega_cambrai(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_cambrai_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_cambrai_1"])

                    self.was_neutral = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_cambrai_2"])

                    Player.add_points(self.player, Dices.face_4(Game.dice_voc, "+"), Dices.face_2(Game.dice_pop_agr), 0,
                                      (-2), 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    self.opposer()
                    break
                elif choice == "3":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_cambrai_3"])

                    Player.add_points(self.player, (-2), (-1), 0, 3, 0)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    break
                elif choice == "4":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_cambrai_4"])

                    Player.add_points(self.player, 0, 0, 0, 0, Dices.face_6(Game.dice_dipl_skill, "+"))
                    Utility.print_points(self.player)

                    Utility.go_on()

                    self.ambassador()
                    break
                else:
                    Utility.error()

        def opposer(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["opposer_input"])
                choice = input()

                self.was_opposer = True

                if choice == "1":
                    prob = random.randint(1, 100)
                    if prob <= 70:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["opposer_1_pos"])

                        Player.add_points(self.player, 0, 3, 0, 0, 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.lega_santa()
                        break
                    elif prob > 70:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["opposer_1_neg"])

                        Utility.gameover()
                        break
                    else:
                        Utility.error()

                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["opposer_2"])

                    Player.add_points(self.player, 0, 0, 0, (-1), 2)
                    Utility.print_points(self.player)

                    Utility.go_on()

                    self.lega_santa()
                    break
                else:
                    Utility.error()

        def battle(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["battle_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["battle_1"])

                    Utility.go_on()

                    self.front_battle()
                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["battle_2"])

                    self.battle_neutral = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                else:
                    Utility.error()

        def front_battle(self):
            prob1 = random.randint(1, 100)

            if prob1 <= 65:
                prob2 = random.randint(1, 100)

                Player.add_points(self.player, 0, (-1), 0, (-1), 0)

                if prob2 <= 75:
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["front_battle_neg_1"])

                    Player.add_points(self.player, 3, 0, (-1), Dices.face_4(Game.dice_cur_rel, "-"), 0)
                    Utility.print_points(self.player)
                    self.battle_injured = True

                    self.lega_santa()
                elif prob2 > 75:
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["front_battle_neg_2"])

                    Utility.gameover()
                else:
                    Utility.error()

            elif prob1 > 65:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["front_battle_pos"])

                self.player.isbishop = False
                self.player.iscardinal = True

                Utility.go_on()

                Game.Conclave(self.player).conclave_start()
            else:
                Utility.error()

        def ambassador(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["ambassador_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["ambassador_france"])

                    Player.add_points(self.player, 0, 0, 2, 0, 0)
                    Utility.print_points(self.player)
                    self.was_france_ambassador = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                elif choice == "2":
                    Player.add_points(self.player, 0, (-2), 0, 0, 0)
                    Utility.print_points(self.player)

                    self.sri_ambassador()
                    break
                else:
                    Utility.error()

        def sri_ambassador(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["ambassador_sri_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["ambassador_sri_strong"])

                    Player.add_points(self.player, 0, 0, 0, 2, Dices.face_2(Game.dice_dipl_skill))
                    Utility.print_points(self.player)
                    self.was_sri_strong = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["ambassador_sri_calm"])

                    Player.add_points(self.player, 0, Dices.face_2(Game.dice_pop_agr), 2, 0, 1)
                    Utility.print_points(self.player)
                    self.was_sri_calm = True

                    Utility.go_on()

                    self.lega_santa()
                    break
                else:
                    Utility.error()

        def lega_santa(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_input"])
                choice = input()

                if choice == "1":
                    if self.was_neutral:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_pro_1"])

                        Player.add_points(self.player, (-1), 0, 2, 2, 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_france_ambassador:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_pro_2"])

                        Player.add_points(self.player, (-1), (-2), (-1), 1, 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_sri_strong:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_pro_3"])

                        Player.add_points(self.player, (-1), 0, Dices.face_4(Game.dice_pol_infl, "-"), 1, (-2))
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_sri_calm:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_pro_4"])

                        Player.add_points(self.player, 1, 1, 0, Dices.face_2(Game.dice_cur_rel), 2)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_opposer:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_pro_5"])

                        Player.add_points(self.player, (-1), (-2), 0, 1, 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.battle_injured:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_pro_6"])

                        Player.add_points(self.player, (-1), 0, 0, 2, 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.battle_neutral:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_pro_7"])

                        Player.add_points(self.player, 0, (-1), 0, 1, 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    else:
                        Utility.error()
                elif choice == "2":
                    if self.was_neutral:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_contro_1"])

                        Player.add_points(self.player, Dices.face_4(Game.dice_voc, "+"), 2, 0, (-1), 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_france_ambassador:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_contro_2"])

                        Player.add_points(self.player, Dices.face_4(Game.dice_voc, "+"), 1, 0, (-2),
                                          Dices.face_4(Game.dice_dipl_skill, "+"))
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_sri_strong:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_contro_3"])

                        Player.add_points(self.player, 1, 2, 0, (-2), Dices.face_4(Game.dice_dipl_skill, "+"))
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_sri_calm:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_contro_4"])

                        Player.add_points(self.player, 3, 0, (-2), (-2), 1)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.was_opposer:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_contro_5"])

                        Player.add_points(self.player, Dices.face_4(Game.dice_voc, "+"), 3, 2,
                                          Dices.face_4(Game.dice_cur_rel, "-"), 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.battle_injured:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_contro_6"])

                        Player.add_points(self.player, Dices.face_6(Game.dice_voc, "+"), 1, 0, (-2), 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    elif self.battle_neutral:
                        Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["lega_santa_contro_7"])

                        Player.add_points(self.player, 1, Dices.face_2(Game.dice_pop_agr), (-1), (-1), 0)
                        Utility.print_points(self.player)

                        Utility.go_on()

                        self.try_become_cardinal()
                        break
                    else:
                        Utility.error()
                else:
                    Utility.error()

        def try_become_cardinal(self):
            if self.player.isbishop and self.player.consensus >= 40:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["become_cardinal_pos"])

                Utility.go_on()

                Game.Conclave(self.player).conclave_start()
            elif self.player.isbishop and self.player.consensus < 40:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["become_cardinal_neg"])
            else:
                Utility.error()

    class Conclave:
        def __init__(self, player):
            self.player = player

            self.cardinal_name = ""
            self.cardinal_values = []

            # Cardinal Values
            (self.card_voc, self.card_pop_agr, self.card_pol_infl,
             self.card_cur_rel, self.card_dipl_skill) = [0, 0, 0, 0, 0]

            # Cardinal that will vote for you
            self.infavor = 0

        def conclave_start(self):
            while True:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["conclave_start_input"])
                choice = input()

                if choice == "1":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["conclave_start_1"])

                    Utility.go_on()

                    Utility.gameover()
                    break
                elif choice == "2":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["conclave_start_2"])

                    Utility.go_on()

                    Game.Conclave(self.player).spanish_alliance()
                    break
                elif choice == "3":
                    Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["conclave_start_3"])

                    Utility.go_on()

                    Game.Conclave(self.player).personal_alliance()
                    break
                else:
                    Utility.error()

        def spanish_alliance(self):
            missions_completed = 0
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance"])

            Utility.go_on()

            # MISSION 1
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_1_input"])

            Utility.go_on()

            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_1"])

            if Test.faith(self.player.voc) == "+":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_1_pos"])
                missions_completed += 1
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_1_neg"])

            Utility.go_on()

            # MISSION 2
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_2"])

            if Test.secrets() == "+":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_2_pos"])
                missions_completed += 1
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_2_neg"])

            Utility.go_on()

            # MISSION 3
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_3"])

            if Test.inlfuence(self.player.pol_infl) == "+":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_3_pos"])
                missions_completed += 1
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_mission_3_neg"])

            if missions_completed >= 2:
                Game.Conclave.pope_nomination()
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["spanish_alliance_gameover"])
                Utility.gameover()

        def personal_alliance(self):
            missions_completed = 0
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance"])

            Utility.go_on()

            # MISSION 1
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_1_input"])

            Utility.go_on()

            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_1"])

            if Test.faith(self.player.voc) == "+":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_1_pos"])
                missions_completed += 1
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_1_neg"])

            Utility.go_on()

            # MISSION 2
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_2"])

            if Test.inlfuence(self.player.pol_infl) == "+":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_2_pos"])
                missions_completed += 1
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_2_neg"])

            Utility.go_on()

            # MISSION 3
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_3"])

            if Test.charisma(self.player.dipl_skill) == "+":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_3_pos"])
                missions_completed += 1
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_mission_3_neg"])

            if missions_completed >= 2:
                Game.Conclave(self.player).alliance_consensus()
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["personal_alliance_gameover"])
                Utility.gameover()

        def alliance_consensus(self):
            missions_completed = 0
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus"])

            Utility.go_on()

            # MISSION 1
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_1_input"])

            Utility.go_on()

            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_1"])

            if Test.secrets() == "+":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_1_pos"])
                missions_completed += 1
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_1_neg"])

            Utility.go_on()

            # MISSION 2
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_2"])

            if Test.inlfuence(self.player.pol_infl) == "+":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_2_pos"])
                missions_completed += 1
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_2_neg"])

            Utility.go_on()

            # MISSION 3
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_3"])

            if Test.strategy() == "+":
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_3_pos"])
                missions_completed += 1
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_mission_3_neg"])

            if missions_completed >= 2:
                Game.Conclave(self.player).alliance_consensus()
                Game.Conclave.pope_nomination()
            else:
                Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["alliance_consensus_gameover"])
                Utility.gameover()

        @staticmethod
        def pope_nomination():
            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["pope_nomination"])

            Utility.fixed_print(Dialogs.load_dialogs(Game.lang)["WIN"])

            Utility.gameover()


# Game start
game = Game()
game.start()
