# Categories in Python

The purpose of this repository is to provide tools for exploring various aspects of categories and category theory in Python. It is built and tested using Python 3.12. 

## Concept

The basic idea is to imitate Haskell type classes using constructors that link Python types with type classes, including monoids, endofunctors and monads, where corresponding constructors are `monoid`, `endofunctor` and `monad`, e.g.:

```
from categories.monoid import monoid

# Define the integers as a monoid under addition
# and 0 as identity

IntM = monoid(t=int, identity=0, op=operator.add)
```

Python objects of the correct type can then be made instances of the Monoid:

```
m1 = IntM(1)   # m1 is of type Monoid[int]
```

Some example usage is given further below. For further worked examples, see
the notebooks under `notebooks/` in this repository.

# Installing

## (Optionally) set up a virtual environment

It is often a good idea to set up a local virtual environment, so as to prevent package contamination in your local Python installation:

1. (Optionally) set up a virtual environment e.g.:

```
python3.12 -m venv .env312
```

2. Activate, e.g.:

```
source .env312/bin/activate
```


## For use locally


Install with `pip`:

```
pip install [path_to_repo]
```

The library itself has no external dependencies, so this will simply install `python_categories` as a package in your project.

## For development with editable install

From within the repo:

```
pip install -e .[dev]
```

This will install `python_categories` with the following dependences:

- pytest (MIT), see [https://pypi.org/project/pytest/](https://pypi.org/project/pytest/)
- mypy (MIT), see [https://pypi.org/project/mypy/](https://pypi.org/project/mypy/)

## For development including notebooks

```
pip install -e .[ju]
```

This will install `python_categories` with the dev dependencies and the resources for running Jupyter notebooks:

- `pytest` (MIT), see [https://pypi.org/project/pytest/](https://pypi.org/project/pytest/)
- `mypy` (MIT), see [https://pypi.org/project/mypy/](https://pypi.org/project/mypy/)
- `jupyter` (BSD)

# Run the tests

So far tests have only been written for `monoid`. From the repo root directory run:

```
pytest
```

# Worked examples

## Monoids

Two instances of a given monoid can be joined using the monoid join operation:

```
m = IntM(1) + IntM(2)     # m = Monoid[int](3)
```

A list of `int`s can be summed using the monoid concatenation operation:

```
total = M.concat([1, 2, 3, 4, 5, 6])    # total = Monoid[int](21)
```

## Endofunctors

A functor is a mapping between categories, that is, a morphism of categories. An endofunctor is a mapping from one category to itself. Many containers in programming languages can be modelled as endofunctors. An endofunctor requires a single method definition, that of `fmap`, which describes how a function from `a` to `b` in category `X` maps to a function from `f a` to `f b` in category `Y`. 


### The `list` functor

A Python `list` is an example of an endofunctor.

```
from categories.functors.endofunctor import Endofunctor, endofunctor

# Define a function that maps a function from `a` to `b` to a `list` of `a` types

def maplist(l: list[U], f: Callable[[U], V]) -> list[V]:
    return list(map(f, l))

# Define the list type as an endofunctor with a map function

ListF = endofunctor[list](fmap=maplist)

# Instantiate a list instance as a list[int] functor
lst = ListF(int, [1, 2, 3])

# Map the str function on to the list
lst_ = lst.fmap(str) 

# lst_ contains a list ['1', '2', '3']
```

### The `Maybe` functor

```
from categories.maybe import Maybe, Just, Nothing, maybe

# Define the maybe type as an endofunctor with a map function
MaybeF = endofunctor[Maybe](maybe.fmap)

# Instantiate a Just value as a Maybe functor
maybe_f = MaybeF(int, Just(1))

# Add one to the value
maybe_f_ = maybe_f.fmap(lambda x: x + 1)

# maybe_f_ contains a value Just(2)
```

## Monads

A monad is a functor with `bind` and `pure`.

### The `list` monad

```
from categories.monad import import Monad, monad
from categories.maybe import Maybe, maybe, Just, Nothing

# Define bind for list, i.e. flat map
def bindlist(l: list[T], f: Callable[[T], list[U]]) -> list[U]:
    return [*chain(*map(f, l))]

# Define a list monad with maplist and bindlist
ListM = monad[list](fmap=maplist, bind=bindlist)

# Instatiate a list as a List monad
list_m = ListM(int, [1, 2, 3])

# Flat map a function onto the list,
# in this case concatenating the range of numbers
# up to x 
list_m_ = list_m.bind(lambda x: [*range(1, x + 1)])

# list_m contains [1, 1, 2, 1, 2, 3]
```

# Resources

For a different approach to the implementation of these ideas, see (https://gitlab.com/danielhones/pycategories/)[https://gitlab.com/danielhones/pycategories/].