from typing import Any

import attrs
from typing_extensions import TypedDict

import typeguard

# from typeguard import typeguard_ignore
typeguard_ignore = typeguard.typeguard_ignore

# def typeguard_ignore(f):
#     return typeguard.typeguard_ignore(f)


class _DictColumnSpec(TypedDict, total=False):
    filters: dict[str, Any]
    tile: int


@typeguard_ignore
def _normalize_columns(input: dict[str, _DictColumnSpec]) -> dict[str, Any]:
    return {}


@attrs.define()
class CreateOptions:
    dims: dict[str, Any] = attrs.field(factory=dict, converter=_normalize_columns)
