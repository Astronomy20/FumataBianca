import pytest
from systems.dice import DiceEngine


class TestDiceEngine:
    def setup_method(self):
        self.engine = DiceEngine()

    def test_roll_d6_range(self):
        for _ in range(300):
            r = self.engine.roll(6)
            assert 1 <= r <= 6

    def test_roll_d4_range(self):
        for _ in range(300):
            r = self.engine.roll(4)
            assert 1 <= r <= 4

    def test_roll_d2_range(self):
        for _ in range(300):
            r = self.engine.roll(2)
            assert r in (1, 2)

    def test_roll_d1_always_one(self):
        for _ in range(20):
            assert self.engine.roll(1) == 1

    def test_render_face_coin_heads(self, capsys):
        self.engine.render_face(2, 1)
        captured = capsys.readouterr()
        assert "☺" in captured.out

    def test_render_face_coin_tails(self, capsys):
        self.engine.render_face(2, 2)
        captured = capsys.readouterr()
        assert "€" in captured.out

    def test_render_face_d4(self, capsys):
        self.engine.render_face(4, 3)
        captured = capsys.readouterr()
        assert "3" in captured.out

    def test_render_face_d6(self, capsys):
        self.engine.render_face(6, 1)
        captured = capsys.readouterr()
        assert "●" in captured.out
