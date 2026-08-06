import pytest
from models.domain import Family, Player, Rank
from ui.console import ConsoleUI
from core.localization import Localization


@pytest.fixture(autouse=True)
def load_lang():
    Localization().load("en")


def _player(rank=Rank.SOLDIER, multipliers=(1.0, 1.0, 1.0, 1.0, 1.0)) -> Player:
    family = Family(name="Test", city="Roma", multipliers=list(multipliers))
    return Player(name="X", family=family, voc=0, pop_agr=0, pol_infl=0, cur_rel=0, dipl_skill=0, rank=rank)


class TestPrintPointsDelta:
    def test_shows_positive_delta_next_to_changed_stat(self, capsys):
        ui = ConsoleUI()
        player = _player()
        player.add_points(voc=3)

        ui.print_points(player)

        assert "Vocation (×1.0): 3 (+3)" in capsys.readouterr().out

    def test_shows_negative_delta_next_to_changed_stat(self, capsys):
        ui = ConsoleUI()
        player = _player()
        player.add_points(voc=5)
        player.add_points(voc=-2)

        ui.print_points(player)

        assert "Vocation (×1.0): 3 (-2)" in capsys.readouterr().out

    def test_no_delta_marker_for_unchanged_stats(self, capsys):
        ui = ConsoleUI()
        player = _player()
        player.add_points(voc=3)

        ui.print_points(player)

        assert "Popular Consensus (×1.0): 0\n" in capsys.readouterr().out

    def test_consensus_delta_matches_included_stats_below_bishop(self, capsys):
        ui = ConsoleUI()
        player = _player()
        player.add_points(voc=3, pop_agr=2, cur_rel=10)

        ui.print_points(player)

        out = capsys.readouterr().out
        assert "5 (+5)" in out

    def test_consensus_delta_includes_cur_rel_and_dipl_skill_from_bishop_up(self, capsys):
        ui = ConsoleUI()
        player = _player(rank=Rank.BISHOP)
        player.add_points(voc=3, pop_agr=2, cur_rel=10)

        ui.print_points(player)

        out = capsys.readouterr().out
        assert "15 (+15)" in out


class TestPrintPointsMultiplier:
    def test_shows_family_multiplier_inline_next_to_each_stat(self, capsys):
        ui = ConsoleUI()
        player = _player(multipliers=(1.1, 1.4, 0.8, 1.0, 1.2))

        ui.print_points(player)

        out = capsys.readouterr().out
        assert "Vocation (×1.1)" in out
        assert "Popular Consensus (×1.4)" in out
        assert "Political Influence (×0.8)" in out
        assert "Curial Relevance (×1.0)" in out
        assert "Diplomatic Skill (×1.2)" in out


class TestPrintPointsConsensusScope:
    def test_shows_which_stats_count_below_bishop(self, capsys):
        ui = ConsoleUI()
        player = _player(rank=Rank.SOLDIER)

        ui.print_points(player)

        out = " ".join(capsys.readouterr().out.split())
        assert "Total Consensus: 0 (Vocation + Popular Consensus + Political Influence)" in out

    def test_shows_all_from_bishop_up(self, capsys):
        ui = ConsoleUI()
        player = _player(rank=Rank.BISHOP)

        ui.print_points(player)

        out = " ".join(capsys.readouterr().out.split())
        assert "Total Consensus: 0 (All)" in out

    def test_shows_all_for_cardinal(self, capsys):
        ui = ConsoleUI()
        player = _player(rank=Rank.CARDINAL)

        ui.print_points(player)

        out = " ".join(capsys.readouterr().out.split())
        assert "Total Consensus: 0 (All)" in out


class TestPrintFamilyMultipliers:
    def test_shows_each_stat_with_its_multiplier(self, capsys):
        ui = ConsoleUI()
        family = Family(name="Gonzaga", city="Mantova", multipliers=[1, 1.1, 1.3, 0.8, 1.2])

        ui.print_family_multipliers(family)

        out = capsys.readouterr().out
        assert "Gonzaga" in out
        assert "1.1" in out
        assert "1.3" in out
        assert "0.8" in out
        assert "1.2" in out

    def test_explains_which_stats_count_initially(self, capsys):
        ui = ConsoleUI()
        family = Family(name="Gonzaga", city="Mantova", multipliers=[1, 1.1, 1.3, 0.8, 1.2])

        ui.print_family_multipliers(family)

        out = " ".join(capsys.readouterr().out.split())
        assert "bishop rank onward" in out
