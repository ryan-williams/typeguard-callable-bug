from .callables import fn1, _fn1, _fn0, fn0


def test_fn0():
    """Passing a Callable (``fn0``) works, as long as its arguments are not ``Optional``."""
    _fn0(fn0, 123)  # ✅ OK


def test_fn1():
    """Functions that take optional arguments are not type-checked properly"""
    _fn1(fn1, 123)  # ❌ TypeCheckError: argument "fn" (function) has too many mandatory positional arguments in its declaration; expected 0 but 1 mandatory positional argument(s) declared
