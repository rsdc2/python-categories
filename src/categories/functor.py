from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any
from copy import deepcopy

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')
W = TypeVar('W')

F = Callable[[T], U]
G = Callable[[V], W]
H = Callable[[F], G]

class Functor(Generic[T, U, V, W]):

    _value: V
    _functor: functor

    def __init__(self, value: V, _functor: functor):
        self._value = value
        self._functor = _functor

    def __str__(self) -> str:
        return f'Functor({self._functor}, {str(self._value)})'

    def fmap(self, f: Callable[[T], U]) -> W:
        return self._functor._fmap(f)(self._value)


class functor(Generic[T, U, V, W]):
    _t: type[T]
    _u: type[U]
    _v: type[V]
    _w: type[W]
    _fmap: H

    def __init__(self, ftypes: tuple[type[T], type[U]], gtypes: tuple[type[V], type[W]], fmap: Callable[[F], G]):
        self._t, self._u = ftypes
        self._v, self._w = gtypes
        self._fmap = fmap

    def __call__(self, v: V) -> Functor[T, U, V, W]:
        return Functor(v, self)

    def __str__(self) -> str:
        return f'functor({self._t} -> {self._u}, {self._fmap})'


if __name__ == '__main__':
    t = list

    def listfmap(f: Callable[[T], U]) -> Callable[[list[T]], list[U]]:

        def _listfmap(l: list[T]) -> list[U]:
            return list(map(f, l))

        return _listfmap

    def add10(x: int) -> int:
        return x + 10
    
    Func = functor((int, int), (list[int], list[int]), listfmap)
    func = Func([1, 2, 3])
    result = func.fmap(add10)
    print(result)