from categories.monoid import *
import operator

M = monoid(int, One, Mul)
N = monoid(int, Zero, Add)
X = monoid(str, EmptyString, Add)

x = M(3) + M(2)
y = N(3) + N(4)
print(x, y)

z = M.concat([1, 2, 3])
a = X.concat(['hello ', 'my friend ', 'Robert'])
print(z, a)