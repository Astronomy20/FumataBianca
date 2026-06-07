from models.domain import Player
from core.localization import loc
from systems.skill_check import skill_check
from ui.console import ui


def run_conclave_start(player: Player) -> None:
    while True:
        ui.print_text(loc.get("conclave_start_input"))
        choice = input()

        if choice == "1":
            ui.print_text(loc.get("conclave_start_1"))

            ui.go_on()

            ui.gameover()
            break
        elif choice == "2":
            ui.print_text(loc.get("conclave_start_2"))

            ui.go_on()

            run_spanish_alliance(player)
            break
        elif choice == "3":
            ui.print_text(loc.get("conclave_start_3"))

            ui.go_on()

            run_personal_alliance(player)
            break
        else:
            ui.error()


def run_spanish_alliance(player: Player) -> None:
    from data.repositories import cardinal_repo
    cards = cardinal_repo.get_all_dict()

    missions_completed = 0
    ui.print_text(loc.get("spanish_alliance"))

    ui.go_on()

    ui.print_text(loc.get("spanish_alliance_mission_1_input"))
    ui.go_on()

    ui.print_text(loc.get("spanish_alliance_mission_1"))

    if skill_check.faith(player.voc, cards) == "+":
        ui.print_text(loc.get("spanish_alliance_mission_1_pos"))
        missions_completed += 1
    else:
        ui.print_text(loc.get("spanish_alliance_mission_1_neg"))

    ui.go_on()

    ui.print_text(loc.get("spanish_alliance_mission_2"))

    if skill_check.secrets(cards) == "+":
        ui.print_text(loc.get("spanish_alliance_mission_2_pos"))
        missions_completed += 1
    else:
        ui.print_text(loc.get("spanish_alliance_mission_2_neg"))

    ui.go_on()

    ui.print_text(loc.get("spanish_alliance_mission_3"))

    if skill_check.influence(player.pol_infl, cards) == "+":
        ui.print_text(loc.get("spanish_alliance_mission_3_pos"))
        missions_completed += 1
    else:
        ui.print_text(loc.get("spanish_alliance_mission_3_neg"))

    if missions_completed >= 2:
        run_pope_nomination()
    else:
        ui.print_text(loc.get("spanish_alliance_gameover"))
        ui.gameover()


def run_personal_alliance(player: Player) -> None:
    from data.repositories import cardinal_repo
    cards = cardinal_repo.get_all_dict()

    missions_completed = 0
    ui.print_text(loc.get("personal_alliance"))

    ui.go_on()

    ui.print_text(loc.get("personal_alliance_mission_1_input"))
    ui.go_on()

    ui.print_text(loc.get("personal_alliance_mission_1"))

    if skill_check.faith(player.voc, cards) == "+":
        ui.print_text(loc.get("personal_alliance_mission_1_pos"))
        missions_completed += 1
    else:
        ui.print_text(loc.get("personal_alliance_mission_1_neg"))

    ui.go_on()

    ui.print_text(loc.get("personal_alliance_mission_2"))

    if skill_check.influence(player.pol_infl, cards) == "+":
        ui.print_text(loc.get("personal_alliance_mission_2_pos"))
        missions_completed += 1
    else:
        ui.print_text(loc.get("personal_alliance_mission_2_neg"))

    ui.go_on()

    ui.print_text(loc.get("personal_alliance_mission_3"))

    if skill_check.charisma(player.dipl_skill, cards) == "+":
        ui.print_text(loc.get("personal_alliance_mission_3_pos"))
        missions_completed += 1
    else:
        ui.print_text(loc.get("personal_alliance_mission_3_neg"))

    if missions_completed >= 2:
        run_alliance_consensus(player)
    else:
        ui.print_text(loc.get("personal_alliance_gameover"))
        ui.gameover()


def run_alliance_consensus(player: Player) -> None:
    from data.repositories import cardinal_repo
    cards = cardinal_repo.get_all_dict()

    missions_completed = 0
    ui.print_text(loc.get("alliance_consensus"))

    ui.go_on()

    ui.print_text(loc.get("alliance_consensus_mission_1_input"))
    ui.go_on()

    ui.print_text(loc.get("alliance_consensus_mission_1"))

    if skill_check.secrets(cards) == "+":
        ui.print_text(loc.get("alliance_consensus_mission_1_pos"))
        missions_completed += 1
    else:
        ui.print_text(loc.get("alliance_consensus_mission_1_neg"))

    ui.go_on()

    ui.print_text(loc.get("alliance_consensus_mission_2"))

    if skill_check.influence(player.pol_infl, cards) == "+":
        ui.print_text(loc.get("alliance_consensus_mission_2_pos"))
        missions_completed += 1
    else:
        ui.print_text(loc.get("alliance_consensus_mission_2_neg"))

    ui.go_on()

    ui.print_text(loc.get("alliance_consensus_mission_3"))

    if skill_check.strategy(cards) == "+":
        ui.print_text(loc.get("alliance_consensus_mission_3_pos"))
        missions_completed += 1
    else:
        ui.print_text(loc.get("alliance_consensus_mission_3_neg"))

    if missions_completed >= 2:
        run_alliance_consensus(player)
        run_pope_nomination()
    else:
        ui.print_text(loc.get("alliance_consensus_gameover"))
        ui.gameover()


def run_pope_nomination() -> None:
    ui.print_text(loc.get("pope_nomination"))
    ui.print_text(loc.get("WIN"))
    ui.gameover()
