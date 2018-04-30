# New Syntax
# ---------------------------------------------------------------------------------------------------------------------

# Keyword-only arguments


def f(a, option=True):
    print(a, option)


f(1)
# 1
# True

f(1, 2)
# 1 2
#
# Oops


def f(a, *, option=True):
    print(a, option)


f(1)
# 1 True

f(1, 2)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: f() takes 1 positional argument but 2 were given
# ---------------------------------------------------------------------------------------------------------------------

# nonlocal statement. Using nonlocal x you can now assign directly to a variable in an outer (but non-global) scope


def outside():
    a = 'outside'

    def inside():
        a = 'inside'
        print(a)

    inside()
    print(a)


outside()
# inside
# outside


def outside():
    a = 'outside'

    def inside():
        nonlocal a
        a = 'inside'
        print(a)

    inside()
    print(a)


outside()
# inside
# inside
# ---------------------------------------------------------------------------------------------------------------------

# Extended Iterable Unpacking

a, b, *rest = range(5)
print(a, b, rest)
# 0 1 [2, 3, 4]

*rest, a = range(5)
print(rest, a)
# [0, 1, 2, 3] 4
# ---------------------------------------------------------------------------------------------------------------------

# Syntax for Delegating to a Subgenerator


# Instead of:
def f(x):
    for i in range(x):
        yield i


def f(x):
    for i in range(x):
        yield i
        yield i


# Just write:
def f(x):
    yield from range(x)


def f(x):
    for i in range(x):
        yield from [i, i]
# ---------------------------------------------------------------------------------------------------------------------

# Matrix Multiplication

import numpy

a = numpy.array([[1, 0], [0, 1]])
b = numpy.array([[4, 1], [2, 2]])
a @ b
# array([[4, 1],
#        [2, 2]])
# ---------------------------------------------------------------------------------------------------------------------

# Formatted string literals

import decimal

name = "Fred"
f"He said his name is {name}."
# 'He said his name is Fred.'
width = 10
precision = 4
value = decimal.Decimal("12.34567")
f"result: {value:{width}.{precision}}"  # nested fields
# 'result:      12.35'
# ---------------------------------------------------------------------------------------------------------------------

# Function argument and return value annotations


def f(a: int, b: 'value with default' = 0) -> 'max(a, b)':
    return max(a, b)


print(f.__annotations__)
# {'a': <class 'int'>, 'b': 'value with default', 'return': 'max(a, b)'}

# Type Hints and Syntax for variable annotations

from typing import List, Dict

primes: List[int] = []

captain: str  # Note: no initial value!


class Starship:
    stats: Dict[str, int] = {}


print(Starship.__annotations__)
# {'stats': typing.Dict[str, int]}
# ---------------------------------------------------------------------------------------------------------------------

# Underscores in Numeric Literals

print(1_000_000_000_000_000)
# 1000000000000000

print(0x_FF_FF_FF_FF)
# 4294967295
# ---------------------------------------------------------------------------------------------------------------------
