from typing import (
    Mapping,
    Union, Any,
)

import attrs
from typing_extensions import TypedDict

import typeguard
# from typeguard import typeguard_ignore
typeguard_ignore = typeguard.typeguard_ignore

# def typeguard_ignore(f):
#     return typeguard.typeguard_ignore(f)


class _DictColumnSpec(TypedDict, total=False):
    filters: Mapping[str, Any]
    tile: int


@typeguard_ignore
def _normalize_columns(input: Mapping[str, _DictColumnSpec]) -> Mapping[str, Any]:
    return {}


@attrs.define()
class CreateOptions:
    dims: Mapping[str, Any] = attrs.field(factory=dict, converter=_normalize_columns)
