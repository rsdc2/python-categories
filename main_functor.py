from categories.endofunctor import Identity, Endofunctor, endofunctor, maybe, Maybe, Just, Nothing, lst, Lst
from categories.monoids.type_monoid import Monoid, monoid
from categories.functions import compose
from typing import TypeVar, Callable, Any, Type
from itertools import chain

T = TypeVar('T')
U = TypeVar('U')

if __name__ == '__main__':


    # f = endofunctor(int, Identity[int])
    # g = endofunctor(int, list[int])
    

    # v = f(1)

    mbe = maybe(int)

    # add1 = lambda x: x + 1

    def add1(x: int):
        return x + 1

    # M = mbe(1)
    M = mbe(1).fmap(add1)

    N: Maybe[None] = mbe(None).fmap(add1) 

    print(M, N)
