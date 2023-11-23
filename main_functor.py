from categories.functor import Identity, Endofunctor, endofunctor, maybe, Maybe, Just, Nothing
from categories.monoid_ import Monoid, monoid
from categories.compose import compose
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

if __name__ == '__main__':

    # # x = Monad.ret(Monad.ret(10))
    # # y = compose(Monad[int].ret, Monad[int].ret)(10)
    # # print(x, y)
    # m = monad[int]()

    # n = monad[Monad[int]]()

    # x = n(m(10))


    # mon = monoid()
    # print(x)

    # l = lst[int]
    # m = Lst(Lst(1))
    # x = m()

    # f = compose(lst(Lst[int]), lst(int))(1)
    # g = l.join(f)
    # print(g)

    # L = l(1)
    # M = m(L)

    # print(l.join(M))

    # mon = monoid[lst[int]](lst(int).ret(), lst(int).join)

    f = endofunctor(int, Identity)

    v = f(1)

    mbe = maybe(int)

    # add1 = lambda x: x + 1

    def add1(x: int):
        return x + 1

    # M = mbe(1)
    M = mbe(1).fmap(add1)

    N: Maybe[None] = mbe(None).fmap(add1) 

    print(M, N)
