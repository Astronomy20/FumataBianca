import pytest
from models.domain import Family, Cardinal, Player, Rank, CheckResult


def _family(multipliers=(1.0, 1.0, 1.0, 1.0, 1.0)) -> Family:
    return Family(name="Test", city="Roma", multipliers=list(multipliers))


class TestPlayerConsensus:
    """consensus no longer applies any multiplier: the multipliers were
    already applied (in add_points) at the moment the points were earned,
    so consensus is a plain sum of the already-weighted stats, checkable
    by hand by the player."""

    def test_non_bishop_uses_three_stats(self):
        f = _family()
        p = Player(name="X", family=f, voc=3, pop_agr=4, pol_infl=5, cur_rel=9, dipl_skill=9)
        assert p.consensus == 3 + 4 + 5

    def test_bishop_uses_all_five_stats(self):
        f = _family()
        p = Player(name="X", family=f, voc=3, pop_agr=4, pol_infl=5, cur_rel=2, dipl_skill=1, rank=Rank.BISHOP)
        assert p.consensus == 3 + 4 + 5 + 2 + 1

    def test_cardinal_uses_all_five_stats(self):
        f = _family()
        p = Player(name="X", family=f, voc=2, pop_agr=3, pol_infl=4, cur_rel=5, dipl_skill=6, rank=Rank.CARDINAL)
        assert p.consensus == 2 + 3 + 4 + 5 + 6

    def test_consensus_updates_on_rank_change(self):
        f = _family()
        p = Player(name="X", family=f, voc=3, pop_agr=4, pol_infl=5, cur_rel=2, dipl_skill=1)
        before = p.consensus
        p.rank = Rank.BISHOP
        assert p.consensus > before

    def test_soldier_and_priest_rank_use_three_stats(self):
        f = _family()
        for rank in (Rank.SOLDIER, Rank.PRIEST, Rank.PARSON):
            p = Player(name="X", family=f, voc=1, pop_agr=2, pol_infl=3, cur_rel=10, dipl_skill=10, rank=rank)
            assert p.consensus == 1 + 2 + 3


class TestPlayerAddPoints:
    def test_adds_all_stats_with_neutral_multipliers(self):
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

    def test_each_gain_is_weighted_by_its_own_family_multiplier(self):
        f = _family(multipliers=[1.1, 1.4, 0.8, 1.0, 1.2])
        p = Player(name="X", family=f, voc=0, pop_agr=0, pol_infl=0, cur_rel=0, dipl_skill=0)
        p.add_points(voc=3, pop_agr=3, pol_infl=3, cur_rel=3, dipl_skill=3)
        assert (p.voc, p.pop_agr, p.pol_infl, p.cur_rel, p.dipl_skill) == (
            round(3 * 1.1), round(3 * 1.4), round(3 * 0.8), round(3 * 1.0), round(3 * 1.2)
        )

    def test_last_gain_records_the_weighted_delta(self):
        f = _family(multipliers=[1.1, 1.0, 1.0, 1.0, 1.0])
        p = Player(name="X", family=f, voc=0, pop_agr=0, pol_infl=0, cur_rel=0, dipl_skill=0)
        p.add_points(voc=3, pop_agr=0, pol_infl=0, cur_rel=0, dipl_skill=0)
        assert p.last_gain == (round(3 * 1.1), 0, 0, 0, 0)

    def test_displayed_stats_sum_to_consensus_by_hand(self):
        f = _family(multipliers=[1.1, 1.4, 0.8, 1.0, 1.2])
        p = Player(name="X", family=f, voc=0, pop_agr=0, pol_infl=0, cur_rel=0, dipl_skill=0)
        p.add_points(voc=6, pop_agr=3, pol_infl=6, cur_rel=5, dipl_skill=8)
        assert p.consensus == p.voc + p.pop_agr + p.pol_infl


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
