from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any
from itertools import chain
from copy import deepcopy

from .monoid import monoid, Monoid

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
        return self._monad._pure(self._monad._pure(x))
    
    def join(self, x: T) -> T:
        pure = self._monad._pure
        return self._monad._join(x)


class monad(Generic[T]):
    _type: type[T]
    _fmap: H
    _pure: I
    _join: G
    _compose: K

    def __init__(self, t: type[T], fmap: H, pure: I, join: G):
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
    
    def listjoin_(x: list[list]) -> list:

        return list(chain(*x))


    def listify(x: Any) -> list[Any]:
        return [x]

    
    M = monad(list, listfmap, listify, listjoin_)
    m = M([[1, 2], [3, 4]])
    joined = m.join(m.compose(1))
    print(joined)

