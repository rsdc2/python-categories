
from categories.monoids.type_monoid import *
import operator

# from categories.functor import Monad, monad
from categories.functions import compose, identity

NaturalMulM = monoid(int, 1, operator.mul)
NaturalAddM = monoid(int, 0, operator.add)
StringM = monoid[str](str, '', operator.add)
ListM = monoid[list](list, [], operator.add)
BinaryFuncM = monoid[Callable[[int], int]](type, identity, compose)



def append10(x: str) -> str:
    return x + '10'

def add10(x: int) -> int:
    return x + 10

def mul10(x: int) -> int:
    return x * 10


mcompose = BinaryFuncM.concat([mul10, add10, add10])
mstring = StringM.concat(['hello', ' Robert'])
n = mcompose(1)
print(NaturalAddM)
print(StringM('hello') + StringM(' Robert'))

# f1 = BinaryFuncM.concat([add10, mul10, add10])
# f2 = (BinaryFuncM(add10) + BinaryFuncM(mul10)) + BinaryFuncM(add10)
# f3 = BinaryFuncM(add10) + (BinaryFuncM(mul10) + BinaryFuncM(add10))
# n = f1.value(10) == f2.value(10) == f3.value(10)
# print(n)

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