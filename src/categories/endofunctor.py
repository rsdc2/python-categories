from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any
from copy import deepcopy

T = TypeVar('T')

F = Callable[[Any], Any]
G = Callable[[T], T]
H = Callable[[F], G]

class Endofunctor(Generic[T]):

    _value: T
    _functor: endofunctor

    def __init__(self, value: T, _functor: endofunctor):
        self._value = value
        self._functor = _functor

    def __str__(self) -> str:
        return f'Functor({self._functor}, {str(self._value)})'

    def fmap(self, f: Callable[[Any], Any]) -> T:
        return self._functor._fmap(f)(self._value)


class endofunctor(Generic[T]):
    _type: type[T]
    _fmap: H

    def __init__(self, t: type[T], fmap: H):
        self._type = t
        self._fmap = fmap

    def __call__(self, v: T) -> Endofunctor[T]:
        return Endofunctor(v, self)

    def __str__(self) -> str:
        return f'functor({self._type}, {self._fmap})'


if __name__ == '__main__':
    t = list

    def listfmap(f: F) -> Callable[[list], list]:

        def _listfmap(l: list) -> list:
            return list(map(f, l))

        return _listfmap
    
    Func = endofunctor(list, listfmap)
    func = Func([1, 2, 3])
    result = func.fmap(lambda x: x+1)