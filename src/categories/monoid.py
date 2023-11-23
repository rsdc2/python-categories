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
from .semigroup import Semigroup
T = TypeVar('T')


class Op(Generic[T]):
    _op: Callable[[T, T], T]

    def __call__(self, x: T, y: T) -> T:
        return self._op(x, y)
    
    @classmethod
    def op(cls) -> Callable[[T, T], T]:
        return cls._op
    

class Empty(Generic[T]):
    _value: T

    @property
    def value(self) -> T:
        return self._value


O = TypeVar('O', bound=Op)

E = TypeVar('E', bound=Empty)


class Mul(Op):
    _op = operator.mul


class Add(Op):
    _op = operator.add
    

class One(Empty):
    _value = 1


class Zero(Empty):
    _value = 0


class EmptyString(Empty):
    _value = ''


class Monoid(Generic[T, E, O]):
    _op: O
    _empty: E
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
    
    def __add__(self, other: Monoid[T, E, O]) -> Monoid[T, E, O]:
        value = self._op(self._value, other._value)
        return Monoid[T, E, O](value)
    
    def __mul__(self, other: Monoid[T, E, O]) -> Monoid[T, E, O]:
        return self.__add__(other)
    
    def __repr__(self) -> str:
        return f'Monoid({self._value})'
    
    def __str__(self) -> str:
        return self.__repr__()


class monoid(Generic[T, E, O]):
    _op: type[O]
    _empty: type[E]
    _type: type[T]

    def __init__(self, t: type[T], empty: type[E], op: type[O]):
        self._type = t
        self._op = op
        self._empty = empty

    def __call__(self, value: T) -> Monoid[T, E, O]:
        m = Monoid[T, E, O](value)
        m._op = self._op()
        m._empty = self._empty()
        m._type = self._type

        return m
    
    def concat(self, seq: Sequence[T]) -> Monoid[T, E, O]:
        return Monoid[T, E, O](reduce(self._op(), seq, self._empty().value))

    @staticmethod    
    def mconcat(m: monoid[T, E, O], seq: Sequence[T]) -> Monoid[T, E, O]:
        return m.concat(seq)
