from typing import TypeVar, Generic, Callable

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


class Just(Generic[T]):

    _value: T

    def __init__(self, value: T) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f'Just({self._value}: {type(self._value).__name__})'


class Nothing(Generic[T]):
    _value: None = None

    def __repr__(self) -> str:
        return 'Nothing'


Maybe = Just[T] | Nothing


class maybe(Generic[U]):

    @classmethod
    def pure(cls, value: U | None) -> Maybe[U]:
        
        if value is None:
            return Nothing()
        
        return Just(value)


    @classmethod
    def fmap(cls, m: Maybe[T], f: Callable[[T | None], U | None]) -> Maybe[U]:

        result = f(m._value)
        if result is None:
            return Nothing[T]()
        
        return Just(result)

    
    @classmethod
    def bind(cls, m: Maybe[T], f: Callable[[T], Maybe[U]]) -> Maybe[U]:
        
        if m._value is None:
            return Nothing[U]()
        
        result = f(m._value)

        if result._value is None:
            return Nothing[U]()
        
        return Just(result._value)
    


