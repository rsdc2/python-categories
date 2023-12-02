from __future__ import annotations
from typing import Generic, TypeVar, Callable, Iterable, Any, overload
from copy import deepcopy

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')
W = TypeVar('W')
X = TypeVar('X')

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
    _u: type[U] | type[T]
    _v: type[V]
    _w: type[W] | type[V]
    _fmap: Callable[[F], G]

    @overload
    def __init__(self, cat1: tuple[type[T], type[U]], cat2: tuple[type[V], type[W]], fmap: Callable[[F], G]):
        ...

    @overload
    def __init__(self, cat1: type[T], cat2: type[V], fmap: Callable[[F], G]):
        ...
    
    def __init__(self, cat1: tuple[type[T], type[U]] | type[T], cat2: tuple[type[V], type[W]] | type[V], fmap: Callable[[F], G]):

        if type(cat1) is tuple and type(cat2) is tuple:            
            self._t, self._u = cat1
            self._v, self._w = cat2
        
        elif type(cat1) is type and type(cat2) is type:
            self._t = cat1
            self._u = cat1
            self._v = cat2
            self._w = cat2

        self._fmap = fmap

    def __call__(self, v: V) -> Functor[T, U, V, W]:
        return Functor(v, self)

    def __str__(self) -> str:
        return f'functor({self._fmap})'


if __name__ == '__main__':
    t = list

    def listfmap(f: Callable[[T], U]) -> Callable[[list[T]], list[U]]:

        def _listfmap(l: list[T]) -> list[U]:
            return list(map(f, l))

        return _listfmap

    def add10(x: int) -> int:
        return x + 10
    
    def int2str(x: int) -> str:
        return str(x)
    
    cat1 = (int, int)
    cat2 = (list[int], list[int])

    cat3 = (int, str)
    cat4 = (list[int], list[str])


    def s(a: type[X]) -> tuple[type[X], type[X]]:
        return (a, a)


    Func1 = functor(cat1, cat2, listfmap)
    func1 = Func1([1, 2, 3])
    result = func1.fmap(add10)
    print(result)

    Func2 = functor(cat3, cat4, listfmap)
    func2 = Func2([1, 2, 3])
    result2 = func2.fmap(str)
    print(result2)

    Func3 = functor(s(int), s(list[int]), listfmap)
    func3 = Func2([1, 2, 3])
    result2 = func2.fmap(str)
    print(result2)