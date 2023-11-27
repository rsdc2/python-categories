from categories.monoid_ import *
import operator

# from categories.functor import Monad, monad
from categories.compose import compose

M = monoid(int, 1, operator.mul)
N = monoid(int, 0, operator.add)
X = monoid[str](str, '', operator.add)
Y = monoid[list](list, [], operator.add)


# Z = monoid(monad.ret, monad.join)

x = M(3) + M(2)
y = N(3) + N(4)
print(x, y)

z = M.concat([1, 2, 3])
a = X.concat(['hello ', 'my friend ', 'Robert'])
b = Y.concat([[], ['hello', 'robert'], ['my friend']])
print(z, a, b)

print(N.test_identity(3))
print(Y.test_identity('hello'))