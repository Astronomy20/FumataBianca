from dataclasses import dataclass
from typing import Dict, List

from models.domain import Cardinal, CheckResult, Player
from core.localization import loc
from systems.skill_check import skill_check
from ui.console import ui

# Modifiers applied to the check's threshold: a "safe" approach lowers it
# (easier), a "bold" approach raises it (harder) but, on success, grants a
# bonus to the stat tied to the approach; on failure, it costs a small
# setback to that same stat.
SAFE_MODIFIER = -3
BOLD_MODIFIER = 3
BOLD_BONUS = 2
BOLD_PENALTY = 2


@dataclass
class Approach:
    check: str  # "faith" | "secrets" | "influence" | "strategy" | "charisma"
    bold: bool
    stat: str  # kwarg name per Player.add_points ("voc", "pol_infl", "dipl_skill", ...)


def _invoke_check(check: str, player: Player, cards: Dict[str, Cardinal], modifier: int) -> CheckResult:
    if check == "faith":
        return skill_check.faith(player.voc, cards, threshold_modifier=modifier)
    if check == "secrets":
        return skill_check.secrets(cards, threshold_modifier=modifier)
    if check == "influence":
        return skill_check.influence(player.pol_infl, cards, threshold_modifier=modifier)
    if check == "strategy":
        return skill_check.strategy(cards, threshold_modifier=modifier)
    if check == "charisma":
        return skill_check.charisma(player.dipl_skill, cards, threshold_modifier=modifier)
    raise ValueError(f"Unknown check: {check}")


def _run_mission(player: Player, cards: Dict[str, Cardinal], mission_key: str, approaches: List[Approach]) -> bool:
    while True:
        ui.print_text(loc.get(mission_key))
        choice = input()

        if choice.isdigit() and 1 <= int(choice) <= len(approaches):
            approach = approaches[int(choice) - 1]
            break
        ui.error()

    modifier = BOLD_MODIFIER if approach.bold else SAFE_MODIFIER
    result = _invoke_check(approach.check, player, cards, modifier)
    success = result == CheckResult.SUCCESS

    ui.print_text(loc.get(f"{mission_key}_pos" if success else f"{mission_key}_neg"))

    if approach.bold:
        delta = BOLD_BONUS if success else -BOLD_PENALTY
        player.add_points(**{approach.stat: delta})
        ui.print_text(loc.get("approach_bold_bonus" if success else "approach_bold_penalty"))
        ui.print_points(player)

    return success


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

    if _run_mission(player, cards, "spanish_alliance_mission_1", [
        Approach("faith", bold=False, stat="voc"),
        Approach("secrets", bold=True, stat="pol_infl"),
        Approach("influence", bold=True, stat="pol_infl"),
    ]):
        missions_completed += 1

    ui.go_on()

    if _run_mission(player, cards, "spanish_alliance_mission_2", [
        Approach("charisma", bold=False, stat="dipl_skill"),
        Approach("influence", bold=False, stat="pol_infl"),
        Approach("secrets", bold=True, stat="pol_infl"),
    ]):
        missions_completed += 1

    ui.go_on()

    if _run_mission(player, cards, "spanish_alliance_mission_3", [
        Approach("influence", bold=True, stat="pol_infl"),
        Approach("faith", bold=False, stat="voc"),
        Approach("secrets", bold=True, stat="pol_infl"),
    ]):
        missions_completed += 1

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

    if _run_mission(player, cards, "personal_alliance_mission_1", [
        Approach("faith", bold=False, stat="voc"),
        Approach("influence", bold=True, stat="pol_infl"),
        Approach("charisma", bold=False, stat="dipl_skill"),
    ]):
        missions_completed += 1

    ui.go_on()

    if _run_mission(player, cards, "personal_alliance_mission_2", [
        Approach("influence", bold=False, stat="pol_infl"),
        Approach("secrets", bold=True, stat="pol_infl"),
    ]):
        missions_completed += 1

    ui.go_on()

    if _run_mission(player, cards, "personal_alliance_mission_3", [
        Approach("faith", bold=False, stat="voc"),
        Approach("secrets", bold=True, stat="dipl_skill"),
        Approach("charisma", bold=False, stat="dipl_skill"),
    ]):
        missions_completed += 1

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

    if _run_mission(player, cards, "alliance_consensus_mission_1", [
        Approach("secrets", bold=True, stat="pol_infl"),
        Approach("influence", bold=False, stat="pol_infl"),
        Approach("charisma", bold=False, stat="dipl_skill"),
    ]):
        missions_completed += 1

    ui.go_on()

    if _run_mission(player, cards, "alliance_consensus_mission_2", [
        Approach("influence", bold=False, stat="pol_infl"),
        Approach("secrets", bold=True, stat="pol_infl"),
        Approach("charisma", bold=False, stat="dipl_skill"),
    ]):
        missions_completed += 1

    ui.go_on()

    if _run_mission(player, cards, "alliance_consensus_mission_3", [
        Approach("faith", bold=False, stat="voc"),
        Approach("secrets", bold=True, stat="voc"),
        Approach("charisma", bold=False, stat="dipl_skill"),
    ]):
        missions_completed += 1

    if missions_completed >= 2:
        run_pope_nomination()
    else:
        ui.print_text(loc.get("alliance_consensus_gameover"))
        ui.gameover()


def run_pope_nomination() -> None:
    ui.print_text(loc.get("pope_nomination"))
    ui.print_text(loc.get("WIN"))
    ui.gameover()
