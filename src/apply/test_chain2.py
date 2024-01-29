from functools import reduce
from collections.abc import Iterator
from itertools import chain, groupby, product


class Stream:
    src = None

    def __init__(self, src):
        self.src = src

    def toList(self):
        return list(self.src)

    def toSet(self):
        return set(self.src)

    def toTuple(self):
        return tuple(self.src)

    def getSource(self):
        return self.src

    def map(self, func):
        return Stream(map(func, self.src))

    def filter(self, predicate):
        return Stream(filter(predicate, self.src))

    def reduce(self, func, identity=None):
        if identity is None:
            return reduce(func, self.src)
        else:
            return reduce(func, self.src, identity)

    def chain(self):
        return Stream(chain.from_iterable(self.src))

    def groupby(self, func=None):
        return Stream(map(lambda it: (it[0], list(it[1])), groupby(self.src, func)))

    def product(self, tag):
        return Stream(product(self.src, tag))

    def all(self, predicate):
        return all(map(lambda it: predicate(it), self.src))

    def any(self, predicate):
        return any(map(lambda it: predicate(it), self.src))

    def first(self, predicate=None):
        if predicate is None:
            if isinstance(self.src, Iterator):
                return next(self.src)
            return next(iter(self.src))
        else:
            return next(filter(predicate, self.src))

    def firstOrNone(self, predicate=None):
        try:
            if predicate is None:
                if isinstance(self.src, Iterator):
                    return next(self.src)
                return next(iter(self.src))
            else:
                return next(filter(predicate, self.src))
        except StopIteration:
            return None
