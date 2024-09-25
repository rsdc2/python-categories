from __future__ import annotations

from typing import (
    TypeVar, 
    Callable, 
    Generic, 
    Sequence, 
    Any
)

from functools import reduce
T = TypeVar('T')


class Monoid(Generic[T]):
    _monoid: monoid[T]
    _value: T

    def __init__(self, value: T, monoid: monoid[T]):
        self._value = value
        self._monoid = monoid

    def __add__(self, other: Monoid[T]) -> Monoid[T]:
        value = self._monoid._op(self._value, other._value)
        return Monoid[T](value, self._monoid)
    
    def __call__(self, v):
        if isinstance(self._value, Callable):
            return self._value(v)
        else:
            raise TypeError(f'{type(self._value)} is not callable. '
                            'A Monoid object can only be called if '
                            'the underlying type is callable.') 

    def __mul__(self, other: Monoid[T]) -> Monoid[T]:
        return self.__add__(other)
    
    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: Any) -> bool:
        if type(other) != type(self):
            return False
        
        return self._monoid == other._monoid and \
            self._value == other._value

    def __repr__(self) -> str:
        return f'Monoid[{type(self._value).__name__}]({self._value})'

    def op(self, x: T, y: T) -> T:
        return self.op(x, y)
    
    @property
    def value(self) -> T:
        return self._value
    
    @value.setter
    def value(self, value: T):
        self._value = value
    

class monoid(Generic[T]):
    """
    Type constructor for a Monoid wrapper around a type T
    """

    _op: Callable[[T, T], T]
    _identity: T
    _type: type[T]

    def __init__(
            self, 
            t: type[T], 
            identity: T, 
            op: Callable[[T, T], T]) -> None: 

        """
        A monoid is a set with a binary join operation and identity such that
        a · e = e · a = a. 

        :param t: the type (= underlying set) of the monoid, e.g. `int`.
        :param identity: identity, e.g. `0`
        :param op: a binary join operation, e.g. `+`
        """
        
        self._type = t
        self._op = op
        self._identity = identity

    def __call__(self, value: T) -> Monoid[T]:

        """
        Wrap a T instance in a Monoid type
        """
        
        return Monoid[T](value, self)
    
    def __eq__(self, other: Any) -> bool:
        
        if type(other) != type(self):
            return False
        
        return self._op == other._op and \
            self._type == other._type and \
            self._identity == other._identity

    def __repr__(self) -> str:

        return f'monoid[{self._type.__name__}](identity: {self._identity}, op: {self._op})'
    
    def concat(self, seq: Sequence[T]) -> Monoid[T]:
        """
        Successively join a sequence of T instances using
        the monoid binary join operation.
        """

        return self(reduce(self._op, seq, self._identity))

    def test_associativity(self, triple: tuple[T, T, T]) -> bool:
        ms = [self(value) for value in triple]
        return ms[0] + (ms[1] + ms[2]) == (ms[0] + ms[1]) + ms[2]
    
    def test_identity(self, test_value: T) -> bool:
        return self(test_value) + self(self._identity) == self(test_value) and \
            self(self._identity) + self(test_value) == self(test_value)