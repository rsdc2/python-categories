from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any, Type
from copy import deepcopy

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')
W = TypeVar('W')
X = TypeVar('X')

F = Callable[[T], T]
G = Callable[[U], U]
H = Callable[[F], G]


class Endofunctor(Generic[T, U]):

    _functor_inst: T
    _functor: endofunctor[T]

    def __init__(self, functor_inst: T, _functor: endofunctor[T]):
        self._functor_inst = functor_inst
        self._functor = _functor

    def __str__(self) -> str:
        return f'Endofunctor({self._functor}, {str(self._functor_inst)})'

    def fmap(self, f: Callable[[U], V]) -> Endofunctor[T, V]:
        fmap = self._functor._fmap

        return Endofunctor[T, V](fmap(self._functor_inst, f), self._functor)


class endofunctor(Generic[T]):
    _fmap: Callable[[T, Callable], T]

    def __init__(self, fmap: Callable[[T, Callable], T]):
        self._fmap = fmap

    def __call__(self, v: T) -> Endofunctor[T, U]:
        return Endofunctor[T, U](v, self)

    def __str__(self) -> str:
        return f'endofunctor({self._fmap})'


if __name__ == '__main__':

    pass