# typeguard-issues
Repros of 2 [typeguard] issues:

## 1. `Callable`s with `Optional` args ([#typeguard#442](https://github.com/agronholm/typeguard/issues/442))

[test_callables.py](src/test_callables.py): passing a `Callable` with `Optional` args to another function, then calling it, results in a `TypeCheckError`:

```
TypeCheckError: argument "fn" (function) has too many mandatory positional arguments in its declaration; expected 0 but 1 mandatory positional argument(s) declared
```

([Github Actions example][GHA callable])

## 2. `typing_extensions.TypedDict` vs. `typeguard_ignore` wrapper ([#typeguard#443](https://github.com/agronholm/typeguard/issues/443))
[test_typeddict.py](src/test_typeddict.py): using `typing_extensions.TypedDict` and a trivial `typeguard_ignore` wrapper results in a `TypeError`:

```
TypeError: TypedDict does not support instance and class checks
```
([Github Actions example][GHA typeddict])

### Docker repro
See [Dockerfile](./Dockerfile):

```Dockerfile
FROM python:3.11.8
RUN git clone https://github.com/ryan-williams/typeguard-issues
WORKDIR typeguard-issues
RUN pip install -e .
RUN pytest src/test_typeddict.py  # ❌ TypeError: TypedDict does not support instance and class checks
```

Attempting to build it repros the error:
```bash
docker build -t typeguard-typeddict-isse .
# > [5/5] RUN pytest src/test_typeddict.py  # ❌ TypeError: TypedDict does not support instance and class checks
# ============================= test session starts ==============================
# platform linux -- Python 3.11.8, pytest-8.1.1, pluggy-1.4.0
# rootdir: /typeguard-issues
# plugins: typeguard-4.1.5
# collected 1 item
#
# src/test_typeddict.py F                                                  [100%]
#
# =================================== FAILURES ===================================
# ________________________________ test_typeddict ________________________________
#
#     def test_typeddict():
# >       Class(field={'aaa': { 'num': 111 }})
#
# src/test_typeddict.py:38:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# <attrs generated init src.test_typeddict.Class>:4: in __init__
#     _setattr('field', __attr_converter_field(field))
# src/test_typeddict.py:26: in converter
#     def converter(arg: dict[str, Spec]) -> dict[str, Any]:
# /usr/local/lib/python3.11/site-packages/typeguard/_functions.py:138: in check_argument_types
#     check_type_internal(value, annotation, memo)
# /usr/local/lib/python3.11/site-packages/typeguard/_checkers.py:759: in check_type_internal
#     checker(value, origin_type, args, memo)
# /usr/local/lib/python3.11/site-packages/typeguard/_checkers.py:231: in check_mapping
#     check_type_internal(v, value_type, memo)
# /usr/local/lib/python3.11/site-packages/typeguard/_checkers.py:763: in check_type_internal
#     if not isinstance(value, origin_type):
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
#
# cls = <class 'src.test_typeddict.Spec'>, other = {'num': 111}
#
#     def __subclasscheck__(cls, other):
#         # Typed dicts are only for static structural subtyping.
# >       raise TypeError('TypedDict does not support instance and class checks')
# E       TypeError: TypedDict does not support instance and class checks
#
# /usr/local/lib/python3.11/site-packages/typing_extensions.py:988: TypeError
# =========================== short test summary info ============================
# FAILED src/test_typeddict.py::test_typeddict - TypeError: TypedDict does not ...
# ============================== 1 failed in 0.06s ===============================
```

[typeguard]: https://github.com/agronholm/typeguard
[GHA callable]: https://github.com/ryan-williams/typeguard-issues/actions/runs/8367660052/job/22910449378#step:6:92
[GHA typeddict]: https://github.com/ryan-williams/typeguard-issues/actions/runs/8367660052/job/22910449378#step:6:121
