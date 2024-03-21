# ❌ ``test_typeddict`` below fails, as written, with error `TypeError: TypedDict does not support instance and class checks`.
#
# For some reason, it passes if either:
# - ✅ ``typing.TypedDict`` is used (instead of ``typing_extensions.TypedDict``)
# - ✅ ``typeguard_ignore`` is imported directly: `from typeguard import typeguard_ignore`


from typing import Any

import attrs
from typing_extensions import TypedDict
# from typing import TypedDict  # ✅ uncommenting this fixes ``test_typeddict`` below

import typeguard

# ✅ uncommenting this also fixes ``test_typeddict`` below (even though it's not used!)
# from typeguard import typeguard_ignore
typeguard_ignore = typeguard.typeguard_ignore


class Spec(TypedDict):
    num: int


@typeguard_ignore
def converter(arg: dict[str, Spec]) -> dict[str, Any]:
    return {}


@attrs.define()
class Class:
    field: dict[str, Any] = attrs.field(factory=dict, converter=converter)


# ❌ As written, this fails with `TypeError: TypedDict does not support instance and class checks`
# Uncommenting either of the "✅" lines above makes it work though 😵‍💫
def test_typeddict():
    Class(field={'aaa': { 'num': 111 }})
