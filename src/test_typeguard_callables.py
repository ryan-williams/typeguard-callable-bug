from .callables import fn_n, _fn_n, _fn_on, fn_on


def test_fn_on():
    _fn_on(fn_on, 123)


def test_fn_n():
    _fn_n(fn_n, 123)
