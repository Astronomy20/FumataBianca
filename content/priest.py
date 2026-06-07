from models.domain import Player, Rank
from core.localization import loc
from systems.dice import dice
from ui.console import ui


def run_why_priest(player: Player) -> None:
    while True:
        ui.print_text(loc.get("why_priest_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("why_priest_1"))

            player.add_points(dice.face_4(loc.get("dice_voc"), "+"), 0, 0, 0, 0)
            ui.print_points(player)

            break
        elif choice == "2":
            ui.print_text(loc.get("why_priest_2"))
            break
        else:
            ui.error()

    ui.go_on()
    run_sermon(player)


def run_sermon(player: Player) -> None:
    while True:
        ui.print_text(loc.get("sermon_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("sermon_1"))

            player.add_points(2, dice.face_4(loc.get("dice_pop_agr"), "+"), 0, 0, 0)
            ui.print_points(player)

            break
        elif choice == "2":
            ui.print_text(loc.get("sermon_2"))

            player.add_points(0, 1, dice.face_4(loc.get("dice_pol_infl"), "-"), 0, 0)
            ui.print_points(player)

            break
        else:
            ui.error()

    ui.go_on()
    run_present(player)


def run_present(player: Player) -> None:
    while True:
        ui.print_text(loc.get("present_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("present_1"))

            player.add_points(1, 2, 0, 0, 0)
            ui.print_points(player)

            break
        elif choice == "2":
            ui.print_text(loc.get("present_2"))

            ui.gameover()
            break
        elif choice == "3":
            ui.print_text(loc.get("present_3"))

            player.add_points(0, 0, -1, 0, 0)
            ui.print_points(player)

            break
        else:
            ui.error()

    ui.go_on()
    run_become_parson(player)


def run_become_parson(player: Player) -> None:
    while True:
        ui.print_text(loc.get("become_parson_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("become_parson_1"))

            player.add_points(
                0,
                dice.face_4(loc.get("dice_pop_agr"), "+"),
                dice.face_4(loc.get("dice_pol_infl"), "+"),
                0,
                0,
            )
            ui.print_points(player)
            player.rank = Rank.PARSON

            ui.go_on()

            run_cardinal_letter(player)
            break
        elif choice == "2":
            ui.print_text(loc.get("become_parson_2"))

            player.add_points(0, 1, 0, 0, 0)
            ui.print_points(player)

            ui.go_on()

            run_annul_marriage(player)
            break
        else:
            ui.error()


def run_cardinal_letter(player: Player) -> None:
    while True:
        ui.print_text(loc.get("cardinal_letter_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("cardinal_letter_1"))

            player.add_points(dice.face_coin(loc.get("dice_voc")), 0, 2, 2, 0)
            ui.print_points(player)

            ui.go_on()

            run_annul_marriage(player)
            break
        elif choice == "2":
            ui.print_text(loc.get("cardinal_letter_2"))

            player.add_points(0, 0, 0, 1, 0)
            ui.print_points(player)

            ui.go_on()

            run_annul_marriage(player)
            break
        elif choice == "3":
            ui.print_text(loc.get("cardinal_letter_3"))

            ui.go_on()

            run_annul_marriage(player)
            break
        else:
            ui.error()


def run_annul_marriage(player: Player) -> None:
    while True:
        ui.print_text(loc.get("annul_marriage_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("annul_marriage_1"))

            ui.gameover()
            break
        elif choice == "2":
            ui.print_text(loc.get("annul_marriage_2_pos"))

            player.add_points(-2, 0, 2, 0, 0)
            ui.print_points(player)

            if player.rank != Rank.PARSON:
                ui.print_text(loc.get("annul_marriage_2_neg"))
                ui.gameover()
            else:
                ui.go_on()
                run_try_become_bishop(player)
            break
        elif choice == "3":
            ui.print_text(loc.get("annul_marriage_3_pos"))

            player.add_points(-2, 0, 1, 0, 0)
            ui.print_points(player)

            if player.rank != Rank.PARSON:
                ui.print_text(loc.get("annul_marriage_3_neg"))
                ui.gameover()
            else:
                ui.go_on()
                run_try_become_bishop(player)
            break
        elif choice == "4":
            ui.print_text(loc.get("annul_marriage_4"))

            player.add_points(1, 0, -3, 0, 0)
            ui.print_points(player)

            ui.go_on()

            run_try_become_bishop(player)
            break
        else:
            ui.error()


def run_try_become_bishop(player: Player) -> None:
    if player.consensus >= 20:
        ui.print_text(loc.get("become_bishop_pos"))

        player.rank = Rank.BISHOP
        ui.go_on()

        from content.bishop import run_bishop
        run_bishop(player)
    else:
        ui.print_text(loc.get("become_bishop_neg"))
        ui.gameover()
