import pytest
from models.domain import Family, Cardinal, Player, Rank, CheckResult


def _family(multipliers=(1.0, 1.0, 1.0, 1.0, 1.0)) -> Family:
    return Family(name="Test", city="Roma", context="ctx", multipliers=list(multipliers))


class TestPlayerConsensus:
    def test_non_bishop_uses_three_stats(self):
        f = _family(multipliers=[1.0, 2.0, 1.0, 1.0, 1.0])
        p = Player(name="X", family=f, voc=3, pop_agr=4, pol_infl=5, cur_rel=9, dipl_skill=9)
        assert p.consensus == round((3 + 4 + 5) * 2.0)

    def test_bishop_uses_all_five_stats(self):
        f = _family(multipliers=[1.0, 2.0, 1.0, 1.0, 1.0])
        p = Player(name="X", family=f, voc=3, pop_agr=4, pol_infl=5, cur_rel=2, dipl_skill=1, rank=Rank.BISHOP)
        assert p.consensus == round((3 + 4 + 5 + 2 + 1) * 2.0)

    def test_cardinal_uses_all_five_stats(self):
        f = _family(multipliers=[1.0, 1.5, 1.0, 1.0, 1.0])
        p = Player(name="X", family=f, voc=2, pop_agr=3, pol_infl=4, cur_rel=5, dipl_skill=6, rank=Rank.CARDINAL)
        assert p.consensus == round((2 + 3 + 4 + 5 + 6) * 1.5)

    def test_consensus_updates_on_rank_change(self):
        f = _family(multipliers=[1.0, 2.0, 1.0, 1.0, 1.0])
        p = Player(name="X", family=f, voc=3, pop_agr=4, pol_infl=5, cur_rel=2, dipl_skill=1)
        before = p.consensus
        p.rank = Rank.BISHOP
        assert p.consensus > before

    def test_soldier_and_priest_rank_use_three_stats(self):
        f = _family(multipliers=[1.0, 1.0, 1.0, 1.0, 1.0])
        for rank in (Rank.SOLDIER, Rank.PRIEST, Rank.PARSON):
            p = Player(name="X", family=f, voc=1, pop_agr=2, pol_infl=3, cur_rel=10, dipl_skill=10, rank=rank)
            assert p.consensus == round((1 + 2 + 3) * 1.0)


class TestPlayerAddPoints:
    def test_adds_all_stats(self):
        p = Player(name="X", family=_family(), voc=1, pop_agr=1, pol_infl=1, cur_rel=1, dipl_skill=1)
        p.add_points(voc=2, pop_agr=3, pol_infl=-1, cur_rel=0, dipl_skill=5)
        assert (p.voc, p.pop_agr, p.pol_infl, p.cur_rel, p.dipl_skill) == (3, 4, 0, 1, 6)

    def test_defaults_are_zero(self):
        p = Player(name="X", family=_family(), voc=5, pop_agr=5, pol_infl=5, cur_rel=5, dipl_skill=5)
        p.add_points()
        assert (p.voc, p.pop_agr, p.pol_infl, p.cur_rel, p.dipl_skill) == (5, 5, 5, 5, 5)

    def test_can_go_negative(self):
        p = Player(name="X", family=_family(), voc=3, pop_agr=3, pol_infl=3, cur_rel=3, dipl_skill=3)
        p.add_points(voc=-10)
        assert p.voc == -7


class TestRank:
    def test_all_six_values_exist(self):
        assert len(Rank) == 6

    def test_bishop_cardinal_in_high_rank_set(self):
        high = (Rank.BISHOP, Rank.CARDINAL)
        assert Rank.BISHOP in high
        assert Rank.CARDINAL in high
        assert Rank.PRIEST not in high
        assert Rank.NOTHING not in high


class TestCheckResult:
    def test_success_value(self):
        assert CheckResult.SUCCESS.value == "+"

    def test_failure_value(self):
        assert CheckResult.FAILURE.value == "-"


class TestCardinal:
    def test_fields(self):
        c = Cardinal(name="Test", voc=7, pop_agr=8, pol_infl=9, cur_rel=6, dipl_skill=5)
        assert c.name == "Test"
        assert c.voc == 7
        assert c.dipl_skill == 5
