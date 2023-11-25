from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any
from itertools import chain
from copy import deepcopy

T = TypeVar('T')

F = Callable[[Any], Any]
G = Callable[[T], T]
H = Callable[[F], G]
I = Callable[[Any], T]
J = Callable[[I, I], I]
K = Callable[[I, I], T]

class Monad(Generic[T]):

    _value: T
    _monad: monad

    def __init__(self, value: T, _monad: monad):
        self._value = value
        self._monad = _monad

    def __str__(self) -> str:
        return f'Functor({self._monad}, {str(self._value)})'

    def fmap(self, f: Callable[[Any], Any]) -> T:
        return self._monad._fmap(f)(self._value)
    
    def pure(self, x: Any) -> T:
        return self._monad._pure(x)

    def compose(self, x: Any) -> T:
        return self._monad._compose(self._monad._pure, self._monad._pure)(x)
    
    def join(self, x: I, y: I) -> I:
        return self._monad._join(x, y)(self._value)


class monad(Generic[T]):
    _type: type[T]
    _fmap: H
    _pure: I
    _join: J
    _compose: K

    def __init__(self, t: type[T], fmap: H, pure: I, join: J):
        self._type = t
        self._fmap = fmap
        self._pure = pure
        self._join = join

    def __call__(self, v: T) -> Monad[T]:
        return Monad(v, self)

    def __str__(self) -> str:
        return f'functor({self._type}, {self._fmap})'

if __name__ == '__main__':
    t = list

    def listfmap(f: Callable[[Any], Any]) -> Callable[[list], list]:

        def _listfmap(l: list) -> list:
            return list(map(f, l))

        return _listfmap
    
    def listjoin(x: Callable[[Any], list], y: Callable[[Any], list]) -> Callable[[Any], list]:

        def _listjoin(z: Any) -> list:
            l = x(y(z))
            l_ = list(chain(*l))
            return l_

        return _listjoin

    def listify(x: Any): list[Any]
        

    
    M = monad(list, listfmap, lambda x: [x], listjoin)
    m = M([[1, 2], [3, 4]])
    joined = m.join(listify, li)