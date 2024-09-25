from __future__ import annotations
from typing import Generic, TypeVar, Callable



M = TypeVar('M')
N = TypeVar('N')
T = TypeVar('T')
U = TypeVar('U')


class Monad(Generic[M, T]):

    _minst: M
    _monad: monad[M]

    def __init__(self, value: M, m: monad[M]):
        self._minst = value
        self._monad = m

    def __repr__(self) -> str:
        return f'Monad[{type(self._minst).__name__}]({str(self._minst)})'
    
    def __str__(self) -> str:
        return self.__repr__()

    def fmap(self, f: Callable[[T], U]) -> Monad[M, U]:
        fmap = self._monad._fmap

        return Monad[M, U](fmap(self._minst, f), self._monad)
    
    def bind(self, f: Callable[[T], M]) -> Monad[M, U]:
        x = self._monad._bind(self._minst, f)
        return Monad[M, U](x, self._monad)


class monad(Generic[M]):
    _fmap: Callable[[M, Callable], M]
    _bind: Callable[[M, Callable], M]

    def __init__(
            self, 
            fmap: Callable[[M, Callable], M],
            bind: Callable[[M, Callable], M]
    ) -> None:
        self._fmap = fmap
        self._bind = bind

    def __call__(self, v: M) -> Monad[M, T]:
        return Monad[M, T](v, self)

    def __str__(self) -> str:
        return f'monad(fmap: {self._fmap.__name__}, bind: {self._bind.__name__})'

