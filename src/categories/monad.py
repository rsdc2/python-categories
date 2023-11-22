from __future__ import annotations

from typing import Generic, TypeVar, Callable, Any
from categories.compose import compose

T = TypeVar('T')


V = TypeVar('V')



class Monad(Generic[T]):
    _v: T
    # def __call__(self, v: T) -> Lst[T]:

    def __init__(self, v: T):
        self._v = v

    def __repr__(self) -> str:
        return f'Endofunctor({self._v})'
    
    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def ret(cls, v: T) -> Monad[T]:
        return Monad(v)

    @classmethod
    def join(cls, x: Callable[[T], Monad[T]], y: Callable[[U], Monad[U]]) -> Callable[[U], Monad[U]]:
        
        def _join(z: U):
            a = y(z)
            b: Monad[Monad[U]] = x(a)

            return b._v
        
        return _join

U = TypeVar('U', bound=Monad)


class monad(Generic[T, U]):
    _v: T
    _t: type[T]

    def __call__(self, v: T) -> U:
        return Monad.ret(v)

    def __repr__(self) -> str:
        return f'Endofunctor({self._v})'
    
    def __str__(self) -> str:
        return self.__repr__()
    
    @staticmethod
    def ret(m: monad, v: T) -> Monad[T]:
        return m(v)

    @staticmethod
    # def compose(x: Callable[[monad[T], T], Monad[T]], y: Callable[[monad[U], U], Monad[U]]) -> Callable[[monad[Any], T], Monad[Monad[T]]]:
    def compose(m: monad[T, U], n: monad[V, U]) -> monad[Monad[T], U]:

        def _compose(x: T):
            M = m(x)
            N = m(M)
                  

    # @staticmethod
    # def join(x: Callable[[monad[T], T], Monad[T]], y: Callable[[monad[U], U], Monad[U]]) -> Callable[[monad[Any], T], Monad[T]]:
    def join(x: monad[T], y: monad[U]) -> monad[U]:
        def _join(z: T):
            a = y(z)
            b = x(a)

            return b._v
        
        return _join

# Callable[[Callable[[monad[Any], T], Monad[T]], Callable[[monad[Any], T], Monad[T]]], Callable[[monad[Any], T], Monad[T]]]