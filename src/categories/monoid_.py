from __future__ import annotations

from typing import (
    TypeVar, 
    Callable, 
    Generic, 
    Sequence, 
    Type, 
    ClassVar, 
    Union
)

import operator
from functools import reduce

T = TypeVar('T')



class Monoid(Generic[T]):
    _op: Callable[[T, T], T]
    _empty: T
    _value: T
    _type: type[T]

    def __init__(self, value: T):
        self._value = value

    def op(self, x: T, y: T) -> T:
        return self.op(x, y)
    
    @property
    def value(self) -> T:
        return self._value
    
    @value.setter
    def value(self, value: T):
        self._value = value
    
    def __add__(self, other: Monoid[T]) -> Monoid[T]:
        value = self._op(self._value, other._value)
        return Monoid[T](value)
    
    def __mul__(self, other: Monoid[T]) -> Monoid[T]:
        return self.__add__(other)
    
    def __repr__(self) -> str:
        return f'Monoid({self._value})'
    
    def __str__(self) -> str:
        return self.__repr__()


# The problem with this 

class monoid(Generic[T]):
    _op: Callable[[T, T], T]
    _empty: T
    _type: type[T]

    def __init__(self, empty: T, op: Callable[[T, T], T]):
        self._type = type(empty)
        self._op = op
        self._empty = empty

    def __call__(self, value: T) -> Monoid[T]:
        m = Monoid[T](value)
        m._op = self._op
        m._empty = self._empty
        m._type = self._type

        return m
    
    def concat(self, seq: Sequence[T]) -> Monoid[T]:
        return Monoid[T](reduce(self._op, seq, self._empty))

    @staticmethod    
    def mconcat(m: monoid[T], seq: Sequence[T]) -> Monoid[T]:
        return m.concat(seq)
