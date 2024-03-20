from typing import Callable, Optional


# ✅ type-checks fine
def _fn0(fn: Callable[[int], bool], s: int) -> bool:
    return fn(s)


def fn0(s: int) -> bool:
    return True


# ❌ TypeCheckError: argument "fn" (function) has too many mandatory positional arguments in its declaration; expected 0 but 1 mandatory positional argument(s) declared
def _fn1(fn: Callable[[Optional[int]], bool], s: Optional[int]) -> bool:
    return fn(s)


def fn1(s: Optional[int]) -> bool:
    return True
