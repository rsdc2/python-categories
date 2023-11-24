from typing import Any, Callable
from itertools import chain
from ..monoid_ import monoid


if __name__ == '__main__':

    def listify(x: Any) -> list[Any]:
        return [x]
    
    
    f = Callable[[Any], list[Any]]

    def join(x: f, y: f) -> f:
        """
        """


        def _join(z: Any) -> list[Any]:
            l = x(y(z))

            l_ = list(chain(*l))

            return l_
        
        return _join


    Mon = monoid[f](listify, join)

    mon = Mon(listify)

    a = Mon.concat([listify, listify])
    print(a)

    print(a.value('z'))
    print(listify('z'))

    
    print(mon)
