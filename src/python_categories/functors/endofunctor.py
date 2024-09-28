from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any, Type
from copy import deepcopy

F = TypeVar('F')
T = TypeVar('T')
U = TypeVar('U')


class Endofunctor(Generic[F, T]):

    _finst: F
    _functor: endofunctor[F]

    def __init__(self, functor_inst: F, _functor: endofunctor[F]):
        self._finst = functor_inst
        self._functor = _functor

    def __repr__(self) -> str:
        return f'Endofunctor[{type(self._finst).__name__}]({str(self._finst)})'

    def __str__(self) -> str:
        return self.__repr__()

    def fmap(self, f: Callable[[T], U]) -> Endofunctor[F, U]:
        fmap = self._functor._fmap

        return Endofunctor[F, U](fmap(self._finst, f), self._functor)

def fmap(functor: Endofunctor[F, T], f: Callable[[T], U]) -> Endofunctor[F, U]:
    return functor.fmap(f)

class endofunctor(Generic[F]):
    _fmap: Callable[[F, Callable], F]

    def __init__(self, fmap: Callable[[F, Callable], F]):
        self._fmap = fmap

    def __call__(self, t: type[T], v: F) -> Endofunctor[F, T]:
        return Endofunctor[F, T](v, self)

    def __str__(self) -> str:
        return f'endofunctor(fmap: {self._fmap.__name__})'


if __name__ == '__main__':

    pass