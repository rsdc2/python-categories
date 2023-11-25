from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any, Iterator
from functools import partial
from ..monoid_ import monoid

T = TypeVar('T')

from functools import reduce

class Monad(Generic[T]):

    _value: Iterable[T]
    _t: Callable[[Any], Iterable[T]]

    def __init__(self, t: Callable[[T], Iterable[T]], value: Iterable[T]):
        self._t = t
        self._value = value

    def __str__(self) -> str:
        return f'Functor({type(self._value)}, {str(self._value)})'
    
    def __add__(self, other: Monad[T]) -> Monad[T]:
        xs = list(self._value)
        ys = list(other._value)

        return Monad(self._t, xs + ys)
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._value)

    def fmap(self, f: Callable[[T], T]) -> Monad[T]:

        items = self._t(map(f, self._value))
        return Monad(self._t, items)
    
    @classmethod
    def join(cls, x: Monad[Monad[T]]) -> Monad[T]:
        
        def _f(acc: Monad[T] | None, item: Monad[T]) -> Monad[T]:
            if acc is None:
                return item
            return acc + item
        
        return reduce(_f, x, None)
            
    
f = Callable[[Any], Monad[Any]]

class monad:
    _t: f

    def __init__(self, t: f):
        self._t = t

    def __call__(self, v: Any) -> Monad[Any]:
        return self._t(v)

    def __repr__(self) -> str:
        return f'monad({self._t})'
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def pure(self, v: Any) -> Monad[Any]:
        return self._t(v)

    @staticmethod
    def join(x: f, y: f) -> f:

        def _join(z: Any) -> Monad[Any]:
            l = x(y(z))

            l_ = l.join(l)

            return l_

        return _join

if __name__ == '__main__':
    # l = [1, 2, 3]

    # f = Monad(list[int], l)
    Md = monad(partial(Monad[int], list))

    md = Md([1, 2, 3])
    # print(f.fmap(lambda x: x + 1))
    Mn = monoid[f](Md.pure, monad.join)

    conc = Mn.concat([Md.pure, Md.pure])

    i = conc([1, 2, 3])