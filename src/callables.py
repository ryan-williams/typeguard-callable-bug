from typing import Callable, Optional


def _fn_os_n(fn: Callable[[Optional[str], int], bool], s: Optional[str], n: int) -> bool:
    return fn(s, n)


def fn_os_n(s: Optional[str], n: int) -> bool:
    return True


def _fn_os(fn: Callable[[Optional[str]], bool], s: Optional[str]) -> bool:
    return fn(s)


def fn_os(s: Optional[str]) -> bool:
    return True


def _fn_on(fn: Callable[[Optional[int]], bool], s: Optional[int]) -> bool:
    return fn(s)


def fn_on(s: Optional[int]) -> bool:
    return True


def _fn_n(fn: Callable[[int], bool], s: int) -> bool:
    return fn(s)


def fn_n(s: int) -> bool:
    return True
