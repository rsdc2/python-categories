from __future__ import annotations
from typing import TypeVar, Callable, Generic, Sequence
from functools import reduce

T = TypeVar('T')


class Semigroup(Generic[T]):
    _op: Callable[[T, T], T]
    _value: T
    _type: type[T]

    def __init__(self, value: T):
        self._value = value

    def __str__(self) -> str:
        return f'Semigroup({self._type.__name__}, {self._value})'

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, other: Semigroup[T]) -> Semigroup[T]:
        value = self._op(self._value, other._value)
        return Semigroup[T](value)
    
    def __mul__(self, other: Semigroup[T]) -> Semigroup[T]:
        return self.__add__(other)

    def op(self, x: T, y: T) -> T:
        return self._op(x, y)

    def concat(self, seq: Sequence[T]) -> T:
        return reduce(self.op, seq, seq[0])
    

class semigroup(Generic[T]):
    _op: Callable[[T, T], T]
    _type: type[T]

    def __init__(self, t: type[T], op: Callable[[T, T], T]):
        self._type = t
        self._op = op

    def __call__(self, value: T) -> Semigroup[T]:
        s = Semigroup[T](value)
        s._op = self._op
        s._type = self._type

        return s
    
    def concat(self, seq: Sequence[T]) -> Semigroup[T]:
        s = Semigroup[T](reduce(self._op, seq, seq[0]))
        s._type = self._type
        s._op = self._op
        return s