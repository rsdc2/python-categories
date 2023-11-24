from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any
from copy import deepcopy

T = TypeVar('T')



class Functor(Generic[T]):

    _value: Iterable[T]
    _t: Callable[[Any], Iterable[T]]

    def __init__(self, t: Callable[[Any], Iterable[T]], value: Iterable[T]):
        self._t = t
        self._value = value

    def __str__(self) -> str:
        return f'Functor({type(self._value)}, {str(self._value)})'

    def fmap(self, f: Callable[[T], T]) -> Functor[T]:

        items = self._t(map(f, self._value))
        return Functor(self._t, items)




if __name__ == '__main__':
    l = [1, 2, 3]

    f = Functor(list[int], l)

    print(f.fmap(lambda x: x + 1))