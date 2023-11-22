from __future__ import annotations
from abc import abstractmethod, abstractclassmethod
from typing import Generic, TypeVar, Callable, Any, Optional
from categories.compose import compose

T = TypeVar('T')


V = TypeVar('V')


class Endofunctor(Generic[T]):
    _t: type[T]
    _value: T

    def __init__(self, value: T):
        self._value = value
        self._t = type(value)

    def fmap(self, f: Callable[[T], T]) -> Endofunctor[T]:
        return Endofunctor(f(self._value))
    
    def __repr__(self) -> str:
        return f'Endofunctor({self._value})'
    

U = TypeVar('U', bound=Endofunctor)




class Identity(Endofunctor):
    pass


class Just(Endofunctor):
    pass
    
class Nothing(Endofunctor):
    _value = None

    def __init__(self):
        pass

    def fmap(self, f: Callable[[T], T]) -> Nothing:
        return Nothing()
    
Maybe = Just | Nothing


class endofunctor(Generic[T, U]):

    _t1: type[T]
    _t2: type[U]

    def __init__(self, t1: type[T], t2: type[U]):
        
        self._t1 = t1
        self._t2 = t2

    def __call__(self, value: T) -> U:
        return self._t2(value)

    def __repr__(self) -> str:
        return f'endofunctor({self._t1.__name__} -> {self._t2.__name__}({self._t1.__name__}))'   

    def __str__(self) -> str:
        return self.__repr__()
     

class maybe(endofunctor):
    _t2 = Just | Nothing

    def __init__(self, t: type[T]):
        self._t1 = t

    def __call__(self, value: T | None) -> Maybe:
        if value is None:
            return Nothing()

        return Just(value)


# class Monad(Generic[T]):
#     _v: T
#     # def __call__(self, v: T) -> Lst[T]:

#     def __init__(self, v: T):
#         self._v = v

#     def __repr__(self) -> str:
#         return f'Monad({self._v})'
    
#     def __str__(self) -> str:
#         return self.__repr__()

#     @abstractmethod
#     @staticmethod
#     def ret(v: T) -> Monad[T]:
#         ...

#     @abstractmethod
#     @staticmethod
#     def join(x: Monad[Monad[T]]) -> Monad[T]:
#         ...
        
# U = TypeVar('U', bound=Monad)








class Lst(Generic[T]):

    _v: T
    # def __call__(self, v: T) -> Lst[T]:

    def __init__(self, v: T):
        self._v = v

    def __repr__(self) -> str:
        return f'Lst({self._v})'
    
    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def ret(v: T) -> Lst[T]:
        return Lst(v)

    @staticmethod
    def join(x: Lst[Lst[T]]) -> Lst[T]:
        return x._v
    # @staticmethod
    # # def compose(x: Callable[[monad[T], T], Monad[T]], y: Callable[[monad[U], U], Monad[U]]) -> Callable[[monad[Any], T], Monad[Monad[T]]]:
    # def compose(m: monad[T, U], n: monad[V, U]) -> monad[Monad[T], U]:

    #     def _compose(x: T):
    #         M = m(x)
    #         N = m(M)
                  

    # # @staticmethod
    # # def join(x: Callable[[monad[T], T], Monad[T]], y: Callable[[monad[U], U], Monad[U]]) -> Callable[[monad[Any], T], Monad[T]]:
    # def join(x: monad[T], y: monad[U]) -> monad[U]:
    #     def _join(z: T):
    #         a = y(z)
    #         b = x(a)

    #         return b._v
        
    #     return _join



class lst(Generic[T]):
    _t: type[T]

    def __init__(self, t: type[T]):
        self._t = t

    def __call__(self, v: T) -> Lst[T]:
        return Lst(v)

    def __repr__(self) -> str:
        return f'lst({self._t})'
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def ret(self) -> lst[T]:
        return lst(self._t)

    
    def join(self, x: lst[Lst[T]], y: lst[T]) -> Callable[[T], Lst[T]]:
        
        # def _join(v: T) -> Lst[T]:
        #     a = y(v)
        #     b = x(a)
        #     return b._v
        
        # return _join
        return lst(self._t)

if __name__ == '__main__':
    l = lst(int)
    L = l(1)
