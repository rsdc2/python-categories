from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any
from copy import deepcopy

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

F = Callable[[T], T]
G = Callable[[U], U]
H = Callable[[F], G]

class Functor(Generic[T, U]):

    _value: U
    _functor: functor

    def __init__(self, value: U, _functor: functor):
        self._value = value
        self._functor = _functor

    def __str__(self) -> str:
        return f'Functor({self._functor}, {str(self._value)})'

    def fmap(self, f: Callable[[T], T]) -> U:
        return self._functor._fmap(f)(self._value)


class functor(Generic[T, U]):
    _t: type[T]
    _u: type[U]
    _fmap: H

    def __init__(self, t: type[T], u: type[U], fmap: Callable[[F], G]):
        self._t = t
        self._u = u
        self._fmap = fmap

    def __call__(self, v: U) -> Functor[T, U]:
        return Functor(v, self)

    def __str__(self) -> str:
        return f'functor({self._t} -> {self._u}, {self._fmap})'


if __name__ == '__main__':
    t = list

    def listfmap(f: F) -> Callable[[list[T]], list[T]]:

        def _listfmap(l: list) -> list:
            return list(map(f, l))

        return _listfmap

    def add10(x: int) -> int:
        return x + 10
    
    Func = functor(int, list[int], listfmap)
    func = Func([1, 2, 3])
    result = func.fmap(add10)
    print(result)