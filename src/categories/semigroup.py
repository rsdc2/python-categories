from __future__ import annotations
from typing import TypeVar, Callable, Generic, Sequence, Any
from functools import reduce

T = TypeVar('T')


class Semigroup(Generic[T]):
    _semigroup: semigroup

    def __init__(self, value: T, sg: semigroup):
        self._value = value
        self._semigroup = sg

    def __str__(self) -> str:
        return f'Semigroup({self._semigroup._type.__name__}, {self._value})'

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, other: Semigroup[T]) -> Semigroup[T]:
        value = self._semigroup._op(self._value, other._value)
        return Semigroup[T](value, self._semigroup)
    
    def __mul__(self, other: Semigroup[T]) -> Semigroup[T]:
        return self.__add__(other)

    def __eq__(self, other: Any) -> bool:
        if type(other) != type(self):
            return False
        
        return self._semigroup == other._semigroup and \
            self._value == other._value

    def op(self, x: T, y: T) -> T:
        return self._semigroup._op(x, y)

    def concat(self, seq: Sequence[T]) -> Semigroup[T]:
        return Semigroup(reduce(self.op, seq, seq[0]), self._semigroup)
    

class semigroup(Generic[T]):
    _op: Callable[[T, T], T]
    _type: type[T]

    def __init__(self, t: type[T], op: Callable[[T, T], T]):
        self._type = t
        self._op = op

    def __call__(self, value: T) -> Semigroup[T]:
        s = Semigroup[T](value, self)
        return s

    def __eq__(self, other: Any) -> bool:
        if type(other) != type(self):
            return False
        return self._op == other._op and self._type == other._type
    
    def concat(self, seq: Sequence[T]) -> Semigroup[T]:
        s = Semigroup[T](reduce(self._op, seq, seq[0]), self)
        return s
    
    def test_associativity(self, triple: tuple[T, T, T]) -> bool:
        ms = [Semigroup[T](value, self) for value in triple]
        return ms[0] + (ms[1] + ms[2]) == (ms[0] + ms[1]) + ms[2]