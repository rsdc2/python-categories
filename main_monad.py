from typing import Callable, TypeVar
from itertools import chain
from categories.monad import Monad, monad
from categories.maybe import Maybe, maybe, Just, Nothing


T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


if __name__ == '__main__':

    def mapf(l: list[U], f: Callable[[U], V]) -> list[V]:
        return list(map(f, l))
    
    def joinlist(ll: list[list[U]]) -> list[U]:
        return [*chain(*ll)]
    
    def bindlist(l: list[T], f: Callable[[T], list[U]]) -> list[U]:
        return [*chain(*map(f, l))]

    ListMonad = monad[list](fmap=mapf, bind=bindlist)
    listmonad: Monad[list, int] = ListMonad([1, 2, 3])

    # print(joinlist([[1, 2, 3], [1, 2, 3]]))

    z: Monad[list, int] = listmonad.bind(lambda x: [x])

    print(z)


    MaybeM = monad[Maybe](fmap=maybe.fmap, bind=maybe.bind)
    
    maybeM: Monad[Maybe, int] = MaybeM(Just(0))

    print(maybeM.bind(lambda x: Nothing() if x == 0 else Just(x)))