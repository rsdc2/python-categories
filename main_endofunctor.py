from categories.endofunctor import Endofunctor, endofunctor
from categories.monoids.type_monoid import Monoid, monoid
from categories.functions import compose
from typing import TypeVar, Callable, Any, Type
from itertools import chain

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

if __name__ == '__main__':

    def mapf(l: list, f: Callable[[U], V]) -> list:
        return list(map(f, l))

    ListFunctor = endofunctor[list](fmap=mapf)
    functor_inst: Endofunctor[list, int] = ListFunctor([1, 2, 3])

    s = functor_inst.fmap(str)

    