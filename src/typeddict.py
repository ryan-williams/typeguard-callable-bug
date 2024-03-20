import attrs as attrs_  # We use the name `attrs` later.
import attrs.validators as vld  # Short name because we use this a bunch.
from typing import TypedDict, Union, Mapping, Optional, Tuple, Iterable, Self

from ignore_wrapper import typeguard_ignore

_DictFilterSpec = Mapping[str, object]
_FilterSpec = Union[str, _DictFilterSpec]


class _DictColumnSpec(TypedDict, total=False):
    filters: Mapping[str, _FilterSpec]
    tile: int


def _normalize_filter(input: _FilterSpec) -> _DictFilterSpec:
    """Normalizes all filters to ``_DictFilterSpec`` format."""
    if isinstance(input, str):
        input = {"_type": input}
    if not isinstance(input, Mapping):
        raise TypeError(
            f"filters must be specified as a string or dict, not {type(input)}"
        )
    try:
        typ_name = input["_type"]
    except KeyError as ke:
        raise ValueError(
            "filter dicts must include a `_type` key with the filter name"
        ) from ke
    if not isinstance(typ_name, str):
        raise TypeError(f"filter name must be a str, not {type(typ_name)}")
    try:
        pass
        # _FILTERS[typ_name]
    except KeyError as ke:
        raise ValueError(f"filter type {typ_name!r} unknown") from ke
    return dict(input)


# These functions have to appear first because they're used in the definition
# of TileDBCreateOptions.
def _normalize_filters(inputs: Iterable[_FilterSpec]) -> Tuple[_DictFilterSpec, ...]:
    if isinstance(inputs, str):
        raise TypeError(
            "filters must be a list of strings (or dicts), not a single string"
        )
    if not isinstance(inputs, Iterable):
        raise TypeError(
            f"filters must be a sequence of filter specs, not {type(inputs)}"
        )
    return tuple(_normalize_filter(spec) for spec in inputs)


# This exists because mypy does not currently (v1.3) support complex converters
# like converters.optional(inner_converter).
def _normalize_filters_optional(
        inputs: Optional[Iterable[_FilterSpec]],
) -> Optional[Tuple[_DictFilterSpec, ...]]:
    return None if inputs is None else _normalize_filters(inputs)


@attrs_.define(frozen=True, slots=True)
class _ColumnConfig:
    filters: Optional[Tuple[_DictFilterSpec, ...]] = attrs_.field(
        converter=_normalize_filters_optional
    )
    tile: Optional[int] = attrs_.field(validator=vld.optional(vld.instance_of(int)))

    @classmethod
    @typeguard_ignore
    def from_dict(cls, input: _DictColumnSpec) -> Self:
        return cls(filters=input.get("filters"), tile=input.get("tile"))


@typeguard_ignore
def _normalize_columns(
        input: Mapping[str, _DictColumnSpec]
) -> Mapping[str, _ColumnConfig]:
    if not isinstance(input, Mapping):
        raise TypeError("column configuration must be a dictionary")
    return {
        col_name: _ColumnConfig.from_dict(value) for (col_name, value) in input.items()
    }
