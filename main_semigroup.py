from categories.semigroup import Semigroup, semigroup
import operator

boolean = semigroup(bool, operator.and_)

true = boolean(True)
print(boolean.concat([True, True, True]))