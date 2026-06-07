import json
import os
import sys
from typing import Optional, Dict, Any


def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath("")
    return os.path.join(base_path, relative_path)


class Localization:
    _instance: Optional["Localization"] = None
    _cache: Dict[str, Dict[str, Any]] = {}
    _lang: str = "en"

    def __new__(cls) -> "Localization":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load(self, lang: str) -> None:
        self._lang = lang
        if lang not in self._cache:
            path = resource_path(f"lang/{lang}.json")
            with open(path, encoding="utf-8") as f:
                self._cache[lang] = json.load(f)

    def get(self, key: str, **kwargs: Any) -> str:
        text = self._cache.get(self._lang, {}).get(key, f"[{key}]")
        if kwargs:
            return text.format(**kwargs)
        return text


loc = Localization()
