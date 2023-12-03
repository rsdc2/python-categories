from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any
from copy import deepcopy

T = TypeVar('T')
U = TypeVar('U', bound=type[T])
X = TypeVar('X')

F = Callable[[T], T]
G = Callable[[U], U]
H = Callable[[F], G]

class Endofunctor(Generic[T, U]):

    _value: U
    _functor: endofunctor

    def __init__(self, value: U, _functor: endofunctor):
        self._value = value
        self._functor = _functor

    def __str__(self) -> str:
        return f'Functor({self._functor}, {str(self._value)})'

    def fmap(self, f: Callable[[T], T]) -> U:
        return self._functor._fmap(f)(self._value)


class endofunctor(Generic[T, U]):
    _fmap: Callable[[F], G]

    def __init__(self, fmap: Callable[[F], G]):
        self._fmap = fmap

    def __call__(self, v: U) -> Endofunctor[T, U]:
        return Endofunctor(v, self)

    def __str__(self) -> str:
        return f'functor({self._fmap})'


if __name__ == '__main__':
    t = list

    def listfmap(f: Callable[[T], T]) -> Callable[[list[T]], list[T]]:

        def _listfmap(l: list[T]) -> list[T]:
            return list(map(f, l))

        return _listfmap
    
    # def string_add(f: Callable)
    

    def add1(x: int) -> int:
        return x + 1
    

    Func = endofunctor[int, list[int]](listfmap)
    func = Func([1, 2, 3])
    result = func.fmap(add1)
    print(result)