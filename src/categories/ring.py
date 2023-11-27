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



class Ring(Generic[T]):
    _group: ring[T]
    _value: T

    def __init__(self, value: T, group: ring[T]):
        self._value = value
        self._group = group
    
    @property
    def value(self) -> T:
        return self._value
    
    @value.setter
    def value(self, value: T):
        self._value = value
    
    def __add__(self, other: Ring[T]) -> Ring[T]:
        g = self._group 
        value = g._add_op(self._value, other._value)
        return Ring[T](value, self._group)
    
    def __mul__(self, other: Ring[T]) -> Ring[T]:
        g = self._group 
        value = g._mult_op(self._value, other._value)
        return Ring[T](value, self._group)
    
    def __repr__(self) -> str:
        return f'Ring({self._value})'
    
    def __str__(self) -> str:
        return self.__repr__()


class ring(Generic[T]):
    _type: type[T]
    _add_op: Callable[[T, T], T]
    _mult_op: Callable[[T, T], T]
    _add_identity: T
    _mult_identity: T
    _add_inverse: Callable[[T], T]

    def __init__(
        self, 
        t: type[T], 
        add_identity: T, 
        mult_identity: T,
        add_op: Callable[[T, T], T], 
        mult_op: Callable[[T, T], T],
        add_inverse: Callable[[T], T]
    ):
        self._type = t
        self._add_op = add_op
        self._mult_op = mult_op
        self._add_inverse = add_inverse
        self._add_identity = add_identity
        self._mult_identity = mult_identity

    def __call__(self, value: T) -> Ring[T]:
        return Ring[T](value, self)
    
    # def concat(self, seq: Sequence[T]) -> Ring[T]:
    #     return Ring[T](reduce(self._op, seq, self._identity), self)
