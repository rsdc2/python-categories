from categories.endofunctor import Endofunctor, endofunctor
from categories.monoids.type_monoid import Monoid, monoid
from categories.functions import compose
from typing import TypeVar, Callable, Any, Type
from itertools import chain

from categories.maybe import Maybe, Just, Nothing, maybe

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


if __name__ == '__main__':

    def mapf(l: list[U], f: Callable[[U], V]) -> list[V]:
        return list(map(f, l))

    ListFunctor = endofunctor[list](fmap=mapf)
    list_functor_inst: Endofunctor[list, int] = ListFunctor(int, [1, 2, 3])

    s = list_functor_inst.fmap(str).fmap(float)

    MaybeFunctor = endofunctor[Maybe](fmap=maybe.fmap)
    maybe_functor_inst = MaybeFunctor(int, maybe.of(1))

    x = maybe_functor_inst.fmap(lambda x: None)