import os
import sys
from typing import Optional

_STD_OUTPUT_HANDLE = -11
_ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

_ansi: Optional[bool] = None
_tty: bool = False


def _enable_windows_vt() -> bool:
    """Ask the Windows console to interpret ANSI escape sequences."""
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(_STD_OUTPUT_HANDLE)
        if handle in (0, -1, None):
            return False

        mode = ctypes.c_uint32()
        # Fails when stdout is a pipe or a file: no console, no ANSI.
        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        if mode.value & _ENABLE_VIRTUAL_TERMINAL_PROCESSING:
            return True
        return bool(kernel32.SetConsoleMode(
            handle, mode.value | _ENABLE_VIRTUAL_TERMINAL_PROCESSING
        ))
    except (ImportError, AttributeError, OSError):
        return False


def _use_utf8() -> None:
    """Frozen builds inherit the console code page (cp850/cp1252 on Windows),
    which cannot encode the dice glyphs. Switch the pipeline to UTF-8."""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError, ValueError):
        return
    if os.name == "nt":
        try:
            import ctypes

            ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        except (ImportError, AttributeError, OSError):
            pass


def init() -> bool:
    """Prepare the terminal once, at start-up. Returns True if ANSI is usable."""
    global _ansi, _tty
    if _ansi is not None:
        return _ansi

    _use_utf8()

    stream = sys.stdout
    _tty = bool(stream is not None and hasattr(stream, "isatty") and stream.isatty())
    if not _tty:
        _ansi = False
    elif os.name == "nt":
        _ansi = _enable_windows_vt()
    else:
        _ansi = os.environ.get("TERM", "") not in ("", "dumb")
    return _ansi


def ansi_enabled() -> bool:
    return init()


def clear_screen() -> None:
    if not _tty:
        return
    # `cls`/`clear` always work regardless of VT support and reliably reset
    # the cursor to the top; the ANSI sequence is added on top when
    # available since some terminals handle it more cleanly than the OS call.
    os.system("cls" if os.name == "nt" else "clear")
    if ansi_enabled():
        print("\033[2J\033[H", end="")


def clear_lines(count: int) -> None:
    """Erase the last `count` printed lines, or the whole screen if the
    terminal cannot move the cursor."""
    if ansi_enabled():
        print("\033[1A\033[2K" * count, end="")
    else:
        clear_screen()


def move_up(count: int) -> str:
    """Escape sequence to move the cursor up, empty when ANSI is unavailable."""
    return f"\033[{count}A" if ansi_enabled() else ""
