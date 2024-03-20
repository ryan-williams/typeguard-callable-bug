# from subscripted_generic import Class, Bound
from typeddict import _normalize_columns


def test_typeguard_ignore_wrapper():
    _normalize_columns(dict(
        a=dict(
            filters=dict(b="c"),
            tile=1
        )
    ))
    # c = Class()
    # c.meth(Bound, lambda s: Bound())
