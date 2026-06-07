import pytest
from core.localization import Localization


class TestLocalization:
    def setup_method(self):
        self.loc = Localization()

    def test_singleton(self):
        assert self.loc is Localization()

    def test_missing_key_returns_fallback(self):
        self.loc.load("en")
        assert self.loc.get("__nonexistent_xyz__") == "[__nonexistent_xyz__]"

    def test_load_english(self):
        self.loc.load("en")
        result = self.loc.get("err")
        assert result
        assert "[err]" not in result

    def test_get_with_kwargs_interpolates(self):
        self.loc.load("en")
        result = self.loc.get("faith_test", faith=99)
        assert "99" in result

    def test_load_all_five_languages(self):
        for lang in ("it", "en", "es", "fr", "de"):
            self.loc.load(lang)
            result = self.loc.get("err")
            assert result and "[err]" not in result, f"Missing 'err' key for {lang}"

    def test_cache_reuse(self):
        self.loc.load("en")
        first = self.loc.get("err")
        self.loc.load("en")
        second = self.loc.get("err")
        assert first == second

    def test_switch_language(self):
        self.loc.load("it")
        it_text = self.loc.get("err")
        self.loc.load("en")
        en_text = self.loc.get("err")
        assert it_text != en_text
