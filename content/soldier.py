import random
from models.domain import Player, Rank
from core.localization import loc
from systems.dice import dice
from ui.console import ui


def run_firenze(player: Player) -> None:
    while True:
        ui.print_text(loc.get("firenze_init"))
        ui.go_on()
        ui.print_text(loc.get("firenze_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("firenze_1"))

            player.add_points(dice.face_4(loc.get("dice_voc"), "+"), 0, 0, 0, 0)
            ui.print_points(player)

            player.rank = Rank.PRIEST
            ui.go_on()

            from content.priest import run_sermon
            run_sermon(player)
            break
        elif choice == "2":
            prob = random.randint(1, 100)
            if prob <= 95:
                ui.print_text(loc.get("firenze_2_pos"))

                player.add_points(dice.face_4(loc.get("dice_voc"), "+"), 0, 0, 0, 0)
                ui.print_points(player)

                player.rank = Rank.PRIEST
                ui.go_on()

                from content.priest import run_sermon
                run_sermon(player)
            elif prob > 95:
                ui.print_text(loc.get("firenze_2_neg"))
                ui.gameover()
            break
        else:
            ui.error()


def run_venezia_milano_mantova(player: Player) -> None:
    while True:
        ui.print_text(loc.get("ven_mil_mant_input", fam_city=player.family.city))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("ven_mil_mant_1_pos"))

            prob = random.randint(1, 100)

            if prob <= 85:
                player.add_points(dice.face_4(loc.get("dice_voc"), "+"), 0, 0, 0, 0)
                ui.print_points(player)

                player.rank = Rank.PRIEST
                ui.go_on()

                from content.priest import run_sermon
                run_sermon(player)
                break
            elif prob > 85:
                ui.print_text(loc.get("ven_mil_mant_1_neg"))
                ui.gameover()
        elif choice == "2":
            ui.print_text(loc.get("ven_mil_mant_2"))

            player.add_points(dice.face_coin(loc.get("dice_voc")), 0, 0, 0, 0)
            ui.print_points(player)

            player.rank = Rank.PRIEST
            ui.go_on()

            from content.priest import run_sermon
            run_sermon(player)
            break
        else:
            ui.error()
