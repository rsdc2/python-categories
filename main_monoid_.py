from categories.monoid_ import *
import operator

M = monoid(int, 1, operator.mul)
N = monoid(int, 0, operator.add)
X = monoid[str](int, '', operator.add)

x = M(3) + M(2)
y = N(3) + N(4)
print(x, y)

z = M.concat([1, 2, 3])
a = X.concat(['hello ', 'my friend ', 'Robert'])
print(z, a)