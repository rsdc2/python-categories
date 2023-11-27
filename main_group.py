from categories.group import group, Group
from categories.monoid_ import monoid, Monoid

import operator

g = group(int, 0, operator.add, operator.neg)

m = monoid(int, 0, operator.add)

M = m

g_ = group(Monoid[int], m(0), m._op, operator.neg)
