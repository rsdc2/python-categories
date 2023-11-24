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



class Group(Generic[T]):
    _group: group[T]
    _value: T

    def __init__(self, value: T, group: group[T]):
        self._value = value
        self._group = group

    def op(self, x: T, y: T) -> T:
        return self.op(x, y)
    
    @property
    def value(self) -> T:
        return self._value
    
    @value.setter
    def value(self, value: T):
        self._value = value
    
    def __add__(self, other: Group[T]) -> Group[T]:
        value = self._group._op(self._value, other._value)
        return Group[T](value, self._group)
    
    def __mul__(self, other: Group[T]) -> Group[T]:
        return self.__add__(other)
    
    def __repr__(self) -> str:
        return f'Group({self._value})'
    
    def __str__(self) -> str:
        return self.__repr__()


class group(Generic[T]):
    _op: Callable[[T, T], T]
    _identity: T
    _type: type[T]
    _inverse: Callable[[T], T]

    def __init__(self, empty: T, op: Callable[[T, T], T], inverse: Callable[[T], T]):
        self._type = type(empty)
        self._op = op
        self._identity = empty
        self._inverse = inverse

    def __call__(self, value: T) -> Group[T]:
        return Group[T](value, self)
    
    def concat(self, seq: Sequence[T]) -> Group[T]:
        return Group[T](reduce(self._op, seq, self._identity), self)
