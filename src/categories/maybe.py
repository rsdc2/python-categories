from typing import TypeVar, Generic, Callable

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar['V']


class Just(Generic[T]):

    _value: T

    def __init__(self, value: T) -> None:
        self._value = value


class Nothing:
    pass


Maybe = Just[T] | Nothing


class maybe(Generic[T]):

    def __call__(self, value: T | None) -> Maybe[T]:
        
        if value is None:
            return Nothing()
        
        return Just(value)


    @classmethod
    def fmap(cls, m: Maybe, f: Callable[[U], V]):
        


