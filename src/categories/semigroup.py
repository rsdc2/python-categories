from __future__ import annotations
from typing import TypeVar, Callable, Generic, Sequence
from functools import reduce

T = TypeVar('T')

# class Semigroup(Generic[T]):
#     _elems: set[T]
#     _op: Callable[[T, T], T]

#     def __init__(self, elems: set[T], op: Callable[[T, T], T]):
#         self._elems = elems
#         self._op = op

#     def __call__(self, x: T, y: T) -> T:
#         return self._op(x, y)

#     def concat(self, seq: Sequence[T]) -> T:
#         try:
#             return reduce(self.__call__, seq[1:], seq[0])
#         except IndexError:
#             raise IndexError("There must be at least one member of the sequence in a semigroup")
        


class Semigroup(Generic[T]):
    _op: Callable[[T, T], T]

    def __init__(self, op: Callable[[T, T], T]):
        self._op = op

    def op(self, x: T, y: T) -> T:
        return self._op(x, y)

    def concat(self, seq: Sequence[T]) -> T:
        return reduce(self.op, seq, seq[0])

    @classmethod    
    def mconcat(cls, m: Semigroup[T], seq: Sequence[T]):
        return m.concat(seq)