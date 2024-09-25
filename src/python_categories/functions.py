from typing import Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


def compose(f: Callable[[U], V], g: Callable[[T], U]) -> Callable[[T], V]:

    def _compose(x: T) -> V:

        return f(g(x))

    return _compose


def identity(x: T) -> T:
    return x