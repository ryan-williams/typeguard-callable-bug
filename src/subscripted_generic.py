import abc
from typing import Callable, Type, TypeVar, Generic, Any, Union

from ignore_wrapper import typeguard_ignore


RawHandle = Union[
    int, str
    # tiledb.Array,
    # tiledb.Group,
    # clib.SOMADataFrame,
    # clib.SOMASparseNDArray,
    # clib.SOMADenseNDArray,
]
_RawHdl_co = TypeVar("_RawHdl_co", bound=RawHandle, covariant=True)


class Wrapper(Generic[_RawHdl_co], metaclass=abc.ABCMeta):
    pass


AnyWrapper = Wrapper[RawHandle]


# class Bound:
#     pass


T = TypeVar("T")


class Object(Generic[T]):
    pass


AnyTileDBObject = Object[AnyWrapper]

# AnyObject = Object[Any]


_TDBO = TypeVar("_TDBO", bound=AnyTileDBObject)


class Class:
    @typeguard_ignore
    def meth(
            self,
            kind: Type[_TDBO],
            factory: Callable[[str], _TDBO],
    ) -> _TDBO:
        pass

