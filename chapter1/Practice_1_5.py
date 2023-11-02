# Section 1.5.1
from operator import mul

def square(x):
    mul(x, x)

def square(x):
    return mul(x, x)

def print_square(x):
    print(square(x))

# Section 1.5.2
# Section 1.5.3

def percent_difference(x, y):
    difference = abs(x-y)
    return 100 * difference / x

result = percent_difference(40, 50)
result
# 25.0

def percent_difference(x, y):
    return 100 * abs(x-y) / x

percent_difference(40, 50)
# 25.0

# Section 1.5.4

def absolute_value(x):
    """Compute abs(x)."""
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x

result = absolute_value(-2)
result
# 2

4 < 2
# False

5 >= 5
# True

0 == -0
# True

True and False
# False
True
# True
not False
# True

# Section 1.5.5
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1 # Fibonacci numbers 1 and 2
    k = 2             # Which Fib number is curr?
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

result = fib(8)
result
# 13

# Section 1.5.6

assert fib(8) == 13, 'The 8th Fibonacci number should be 13'

def fib_test():
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
    assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'

def sum_naturals(n):
    """Return the sum of the first n natural numbers.

    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

from doctest import testmod
testmod()
# TestResults(failed=0, attempted=2)

from doctest import run_docstring_examples
run_docstring_examples(sum_naturals, globals(), True)
# Finding tests in NoName
# Trying:
#     sum_naturals(10)
# Expecting:
#     55
# ok
# Trying:
#     sum_naturals(100)
# Expecting:
#     5050
# ok
