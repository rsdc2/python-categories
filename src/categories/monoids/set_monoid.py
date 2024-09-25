from __future__ import annotations

from typing import (
    TypeVar, 
    Callable, 
    Generic, 
    Sequence, 
    Type, 
    ClassVar, 
    Union,
    Any
)

import operator
from functools import reduce
from ....dev.src.categories.semigroup import Semigroup, semigroup
T = TypeVar('T')
U = TypeVar('U')

from enum import Enum


class Monoid(Generic[T]):
    _monoid: monoid[T]
    _value: T

    def __init__(self, value: T, monoid: monoid[T]):
        self._value = value
        self._monoid = monoid

    def op(self, x: T, y: T) -> T:
        return self.op(x, y)
    
    @property
    def value(self) -> T:
        return self._value
    
    @value.setter
    def value(self, value: T):
        self._value = value
    
    def __add__(self, other: Monoid[T]) -> Monoid[T]:
        value = self._monoid._op(self._value, other._value)
        return Monoid[T](value, self._monoid)
    
    def __mul__(self, other: Monoid[T]) -> Monoid[T]:
        return self.__add__(other)
    
    def __repr__(self) -> str:
        return f'Monoid({self._value})'
    
    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: Any) -> bool:
        if type(other) != type(self):
            return False
        
        return self._monoid == other._monoid and \
            self._value == other._value



class monoid(Generic[T]):
    _op: Callable[[T, T], T]
    _identity: T
    _type: type[T]

    def __init__(self, s: set[T], identity: T, op: Callable[[T, T], T]):
        self._set = s
        self._op = op
        self._identity = identity

    def __call__(self, value: T) -> Monoid[T]:
        return Monoid[T](value, self)
    
    def __eq__(self, other: Any) -> bool:
        
        if type(other) != type(self):
            return False
        
        return self._op == other._op and \
            self._type == other._type and \
            self._identity == other._identity
    
    def concat(self, seq: Sequence[T]) -> Monoid[T]:
        return self(reduce(self._op, seq, self._identity))

    def test_associativity(self, triple: tuple[T, T, T]) -> bool:
        ms = [self(value) for value in triple]
        return ms[0] + (ms[1] + ms[2]) == (ms[0] + ms[1]) + ms[2]
    
    def test_identity(self, test_value: T) -> bool:
        return self(test_value) + self(self._identity) == self(test_value) and \
            self(self._identity) + self(test_value) == self(test_value)