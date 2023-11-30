from typing import TypeVar
import typing
from categories.monoid import *
import operator

A = TypeVar('A')
B = TypeVar('B')

FType = Callable[[A], A]

# from categories.functor import Monad, monad
from categories.functions import compose, identity

M = monoid(int, 1, operator.mul)
N = monoid(int, 0, operator.add)
X = monoid[str](str, '', operator.add)
Y = monoid[list](list, [], operator.add)
Z = monoid[Callable[[int], int]](type, identity, compose)

def append10(x: str) -> str:
    return x + '10'

def add10(x: int) -> int:
    return x + 10

def mult10(x: int) -> int:
    return x * 10

f1 = Z.concat([add10, mult10, add10])
f2 = (Z(add10) + Z(mult10)) + Z(add10)
f3 = Z(add10) + (Z(mult10) + Z(add10))
n = f1.value(10) == f2.value(10) == f3.value(10)
print(n)

# print(Z.test_associativity((add10, mult10, add10)))
# print(Z.test_identity(add10))

# # Z = monoid(monad.ret, monad.join)

# x = M(3) + M(2)
# y = N(3) + N(4)
# print(x, y)

# z = M.concat([1, 2, 3])
# a = X.concat(['hello ', 'my friend ', 'Robert'])
# b = Y.concat([[], ['hello', 'robert'], ['my friend']])
# print(z, a, b)

# print(N.test_identity(3))
# print(Y.test_identity(['hello']))