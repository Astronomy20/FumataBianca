import pytest
from unittest.mock import patch
from systems.dice import DiceEngine
from core.localization import Localization


@pytest.fixture(autouse=True)
def load_lang():
    Localization().load("en")


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


class TestDiceEngineMultipleDice:
    def setup_method(self):
        self.engine = DiceEngine()

    def test_render_faces_shows_each_dies_own_correct_result(self, capsys):
        self.engine.render_faces(4, [3, 4])
        captured = capsys.readouterr()
        assert "3" in captured.out
        assert "4" in captured.out

    def test_render_faces_draws_dice_side_by_side_on_the_same_line(self, capsys):
        self.engine.render_faces(4, [1, 2])
        captured = capsys.readouterr()
        combined_lines = [line for line in captured.out.splitlines() if "1" in line and "2" in line]
        assert combined_lines, "expected a single line containing both dice, not two stacked lines"

    def test_render_faces_single_die_matches_render_face(self, capsys):
        self.engine.render_faces(6, [4])
        multi_out = capsys.readouterr().out
        self.engine.render_face(6, 4)
        single_out = capsys.readouterr().out
        assert multi_out == single_out


class TestDiceEngineSignedResults:
    def setup_method(self):
        self.engine = DiceEngine()

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_face_coin_heads_returns_positive_one(self, mock_print, mock_input):
        with patch.object(self.engine, "roll", return_value=1), \
             patch.object(self.engine, "animate"), \
             patch.object(self.engine, "render_face"):
            assert self.engine.face_coin("test") == 1

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_face_coin_tails_returns_negative_one(self, mock_print, mock_input):
        with patch.object(self.engine, "roll", return_value=2), \
             patch.object(self.engine, "animate"), \
             patch.object(self.engine, "render_face"):
            assert self.engine.face_coin("test") == -1

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_face_4_positive_val_returns_positive_result(self, mock_print, mock_input):
        with patch.object(self.engine, "roll", return_value=3), \
             patch.object(self.engine, "animate"), \
             patch.object(self.engine, "render_face"):
            assert self.engine.face_4("test", "+") == 3

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_face_4_negative_val_returns_negative_result(self, mock_print, mock_input):
        with patch.object(self.engine, "roll", return_value=3), \
             patch.object(self.engine, "animate"), \
             patch.object(self.engine, "render_face"):
            assert self.engine.face_4("test", "-") == -3

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_face_6_positive_val_returns_positive_result(self, mock_print, mock_input):
        with patch.object(self.engine, "roll", return_value=5), \
             patch.object(self.engine, "animate"), \
             patch.object(self.engine, "render_face"):
            assert self.engine.face_6("test", "+") == 5

    @patch("builtins.input", return_value="")
    @patch("builtins.print")
    def test_face_6_negative_val_returns_negative_result(self, mock_print, mock_input):
        with patch.object(self.engine, "roll", return_value=5), \
             patch.object(self.engine, "animate"), \
             patch.object(self.engine, "render_face"):
            assert self.engine.face_6("test", "-") == -5
