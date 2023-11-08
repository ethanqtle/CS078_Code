print("\nSection 2.2.1")
print("1/3\n# ", 1 / 3)
# 0.3333333333333333
print("1/3 == 0.3333333333333333\n# ", 1 / 3 == 0.3333333333333333)
# True


def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def print_rational(x):
    print(numer(x), '/', denom(x))


def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


print("\nSection 2.2.2")
print("[10, 20]\n #", [10, 20])

pair = [10, 20]
print("pair\n #", pair)
# [10, 20]
x, y = pair
print("x\n #", x)
# 10
print("y\n #", y)
# 20

print("pair[0]\n #", pair[0])
print("pair[1]\n #", pair[1])

from operator import getitem
print("getitem(pair, 0)\n #", getitem(pair, 0))
# 10
print("getitem(pair, 1)\n #", getitem(pair, 1))
# 20


def rational(n, d):
    """A representation of the rational number N/D."""
    return [n, d]


def numer(x):
    """Return the numerator of rational number X."""
    return x[0]


def denom(x):
    """Return the denominator of rational num X."""
    return x[1]


half = rational(1, 2)
print_rational(half)
# 1 / 2
third = rational(1, 3)
print_rational(mul_rationals(half, third))
# 1 / 6
print_rational(add_rationals(third, third))
# 6 / 9

from math import gcd


def rational(n, d):
    """A representation of the rational number N/D."""
    g = gcd(n, d)
    return [n // g, d // g]


print_rational(add_rationals(third, third))
# 2 / 3

print("\nSection 2.2.3")


def square_rational(x):
    return mul_rational(x, x)


def square_rational_violating_once(x):
    """Referring directly to numerators 
    and denominators would violate one abstraction barrier."""
    return rational(numer(x) * numer(x), denom(x) * denom(x))


def square_rational_violating_twice(x):
    """Assuming that rationals are represented as 
    two-element lists would violate two abstraction barriers.
    """
    return [x[0] * x[0], x[1] * x[1]]


print("\nSection 2.2.4")


def pair(x, y):
    """Return a function that represents a pair."""

    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y

    return get


def select(p, i):
    """Return the element at index i of pair p."""
    return p(i)

p = pair(20, 14)
print("select(p, 0)\n# " , select(p, 0))
# 20
print("select(p, 1)\n# " , select(p, 1))
# 14
