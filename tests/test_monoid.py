from categories.monoids.type_monoid import monoid, Monoid
import random
import pytest
from typing import Type, TypeVar, Callable
import operator


T = TypeVar('T')

def randint() -> int:
    return random.randint(0, 200)


def get_random(total: int, random_genrator: Callable[[], T]) -> list[T]:
    return [random_genrator() for _ in range(total)] 


def get_triples(total: int, random_generator: Callable[[], T]) -> list[tuple[T, T, T]]:
    f = random_generator

    return [(f(), f(), f()) for _ in range(total)]


@pytest.mark.parametrize("triple", get_triples(100, randint))
def test_monoid_associative(
    # t: Type, 
    # identity: T, 
    # op: Callable[[T, T], T], 
    triple: tuple[T, T, T]
):
    
    M = monoid(int, 0, operator.add)

    assert M.test_associativity(triple) == True


@pytest.mark.parametrize("random_value", get_random(200, randint))
def test_monoid_identity(
    random_value: T
):
    M = monoid(int, 0, operator.add)

    assert M.test_identity(random_value) == True
