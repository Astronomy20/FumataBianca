import random
from dataclasses import dataclass
from models.domain import Player, Rank
from core.localization import loc
from systems.dice import dice
from ui.console import ui


@dataclass
class BishopState:
    was_neutral: bool = False
    was_france_ambassador: bool = False
    was_sri_strong: bool = False
    was_sri_calm: bool = False
    was_opposer: bool = False
    battle_neutral: bool = False
    battle_injured: bool = False


def run_bishop(player: Player) -> None:
    state = BishopState()
    run_residence(player, state)


def run_residence(player: Player, state: BishopState) -> None:
    while True:
        ui.print_text(loc.get("residence_input", fam_city=player.family.city))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("residence_1"))

            player.add_points(2, 0, 0, 0, 0)
            ui.print_points(player)

            ui.go_on()

            run_taxation(player, state)
            break
        elif choice == "2":
            ui.print_text(loc.get("residence_2"))

            player.add_points(0, -2, 0, 3, 0)
            ui.print_points(player)

            ui.go_on()

            run_help_cardinal(player, state)
            break
        else:
            ui.error()


def run_taxation(player: Player, state: BishopState) -> None:
    while True:
        ui.print_text(loc.get("taxation_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("taxation_1"))

            player.add_points(0, -2, 2, 1, 1)
            ui.print_points(player)

            ui.go_on()

            break
        elif choice == "2":
            ui.print_text(loc.get("taxation_2"))

            player.add_points(0, 2, -1, -1, 0)
            ui.print_points(player)

            ui.go_on()

            break
        else:
            ui.error()

    run_lega_cambrai(player, state)


def run_help_cardinal(player: Player, state: BishopState) -> None:
    while True:
        ui.print_text(loc.get("help_cardinal_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("help_cardinal_1"))

            player.add_points(0, -1, dice.face_coin(loc.get("dice_pol_infl")), 1, 0)
            ui.print_points(player)

            ui.go_on()

            break
        elif choice == "2":
            ui.print_text(loc.get("help_cardinal_2"))

            player.add_points(dice.face_4(loc.get("dice_voc"), "+"), 1, 0, -2, 0)
            ui.print_points(player)

            ui.go_on()

            break
        else:
            ui.error()

    run_lega_cambrai(player, state)


def run_lega_cambrai(player: Player, state: BishopState) -> None:
    while True:
        ui.print_text(loc.get("lega_cambrai_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("lega_cambrai_1"))

            state.was_neutral = True

            ui.go_on()

            run_lega_santa(player, state)
            break
        elif choice == "2":
            ui.print_text(loc.get("lega_cambrai_2"))

            player.add_points(
                dice.face_4(loc.get("dice_voc"), "+"),
                dice.face_coin(loc.get("dice_pop_agr")),
                0,
                -2,
                0,
            )
            ui.print_points(player)

            ui.go_on()

            run_opposer(player, state)
            break
        elif choice == "3":
            ui.print_text(loc.get("lega_cambrai_3"))

            player.add_points(-2, -1, 0, 3, 0)
            ui.print_points(player)

            ui.go_on()

            break
        elif choice == "4":
            ui.print_text(loc.get("lega_cambrai_4"))

            player.add_points(0, 0, 0, 0, dice.face_6(loc.get("dice_dipl_skills"), "+"))
            ui.print_points(player)

            ui.go_on()

            run_ambassador(player, state)
            break
        else:
            ui.error()


def run_opposer(player: Player, state: BishopState) -> None:
    while True:
        ui.print_text(loc.get("opposer_input"))
        choice = input()

        state.was_opposer = True

        if choice == "1":
            prob = random.randint(1, 100)
            if prob <= 70:
                ui.print_text(loc.get("opposer_1_pos"))

                player.add_points(0, 3, 0, 0, 0)
                ui.print_points(player)

                ui.go_on()

                run_lega_santa(player, state)
                break
            elif prob > 70:
                ui.print_text(loc.get("opposer_1_neg"))

                ui.gameover()
                break
        elif choice == "2":
            ui.print_text(loc.get("opposer_2"))

            player.add_points(0, 0, 0, -1, 2)
            ui.print_points(player)

            ui.go_on()

            run_lega_santa(player, state)
            break
        else:
            ui.error()


def run_battle(player: Player, state: BishopState) -> None:
    while True:
        ui.print_text(loc.get("battle_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("battle_1"))

            ui.go_on()

            run_front_battle(player, state)
            break
        elif choice == "2":
            ui.print_text(loc.get("battle_2"))

            state.battle_neutral = True

            ui.go_on()

            run_lega_santa(player, state)
            break
        else:
            ui.error()


def run_front_battle(player: Player, state: BishopState) -> None:
    prob1 = random.randint(1, 100)

    if prob1 <= 65:
        prob2 = random.randint(1, 100)

        player.add_points(0, -1, 0, -1, 0)

        if prob2 <= 75:
            ui.print_text(loc.get("front_battle_neg_1"))

            player.add_points(3, 0, -1, dice.face_4(loc.get("dice_cur_rel"), "-"), 0)
            ui.print_points(player)
            state.battle_injured = True

            run_lega_santa(player, state)
        elif prob2 > 75:
            ui.print_text(loc.get("front_battle_neg_2"))

            ui.gameover()
    elif prob1 > 65:
        ui.print_text(loc.get("front_battle_pos"))

        player.rank = Rank.CARDINAL
        ui.go_on()

        from content.conclave import run_conclave_start
        run_conclave_start(player)


def run_ambassador(player: Player, state: BishopState) -> None:
    while True:
        ui.print_text(loc.get("ambassador_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("ambassador_france"))

            player.add_points(0, 0, 2, 0, 0)
            ui.print_points(player)
            state.was_france_ambassador = True

            ui.go_on()

            run_lega_santa(player, state)
            break
        elif choice == "2":
            player.add_points(0, -2, 0, 0, 0)
            ui.print_points(player)

            run_sri_ambassador(player, state)
            break
        else:
            ui.error()


def run_sri_ambassador(player: Player, state: BishopState) -> None:
    while True:
        ui.print_text(loc.get("ambassador_sri_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("ambassador_sri_strong"))

            player.add_points(0, 0, 0, 2, dice.face_coin(loc.get("dice_dipl_skills")))
            ui.print_points(player)
            state.was_sri_strong = True

            ui.go_on()

            run_lega_santa(player, state)
            break
        elif choice == "2":
            ui.print_text(loc.get("ambassador_sri_calm"))

            player.add_points(0, dice.face_coin(loc.get("dice_pop_agr")), 2, 0, 1)
            ui.print_points(player)
            state.was_sri_calm = True

            ui.go_on()

            run_lega_santa(player, state)
            break
        else:
            ui.error()


def run_lega_santa(player: Player, state: BishopState) -> None:
    while True:
        ui.print_text(loc.get("lega_santa_input"))
        choice = input()

        if choice == "1":
            if state.was_neutral:
                ui.print_text(loc.get("lega_santa_pro_1"))

                player.add_points(-1, 0, 2, 2, 0)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.was_france_ambassador:
                ui.print_text(loc.get("lega_santa_pro_2"))

                player.add_points(-1, -2, -1, 1, 0)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.was_sri_strong:
                ui.print_text(loc.get("lega_santa_pro_3"))

                player.add_points(-1, 0, dice.face_4(loc.get("dice_pol_infl"), "-"), 1, -2)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.was_sri_calm:
                ui.print_text(loc.get("lega_santa_pro_4"))

                player.add_points(1, 1, 0, dice.face_coin(loc.get("dice_cur_rel")), 2)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.was_opposer:
                ui.print_text(loc.get("lega_santa_pro_5"))

                player.add_points(-1, -2, 0, 1, 0)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.battle_injured:
                ui.print_text(loc.get("lega_santa_pro_6"))

                player.add_points(-1, 0, 0, 2, 0)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.battle_neutral:
                ui.print_text(loc.get("lega_santa_pro_7"))

                player.add_points(0, -1, 0, 1, 0)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            else:
                ui.error()
        elif choice == "2":
            if state.was_neutral:
                ui.print_text(loc.get("lega_santa_contro_1"))

                player.add_points(dice.face_4(loc.get("dice_voc"), "+"), 2, 0, -1, 0)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.was_france_ambassador:
                ui.print_text(loc.get("lega_santa_contro_2"))

                player.add_points(
                    dice.face_4(loc.get("dice_voc"), "+"),
                    1,
                    0,
                    -2,
                    dice.face_4(loc.get("dice_dipl_skills"), "+"),
                )
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.was_sri_strong:
                ui.print_text(loc.get("lega_santa_contro_3"))

                player.add_points(1, 2, 0, -2, dice.face_4(loc.get("dice_dipl_skills"), "+"))
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.was_sri_calm:
                ui.print_text(loc.get("lega_santa_contro_4"))

                player.add_points(3, 0, -2, -2, 1)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.was_opposer:
                ui.print_text(loc.get("lega_santa_contro_5"))

                player.add_points(
                    dice.face_4(loc.get("dice_voc"), "+"),
                    3,
                    2,
                    dice.face_4(loc.get("dice_cur_rel"), "-"),
                    0,
                )
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.battle_injured:
                ui.print_text(loc.get("lega_santa_contro_6"))

                player.add_points(dice.face_6(loc.get("dice_voc"), "+"), 1, 0, -2, 0)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            elif state.battle_neutral:
                ui.print_text(loc.get("lega_santa_contro_7"))

                player.add_points(1, dice.face_coin(loc.get("dice_pop_agr")), -1, -1, 0)
                ui.print_points(player)

                ui.go_on()

                run_try_become_cardinal(player, state)
                break
            else:
                ui.error()
        else:
            ui.error()


def run_try_become_cardinal(player: Player, state: BishopState) -> None:
    if player.rank == Rank.BISHOP and player.consensus >= 40:
        ui.print_text(loc.get("become_cardinal_pos"))

        player.rank = Rank.CARDINAL
        ui.go_on()

        from content.conclave import run_conclave_start
        run_conclave_start(player)
    else:
        ui.print_text(loc.get("become_cardinal_neg"))
