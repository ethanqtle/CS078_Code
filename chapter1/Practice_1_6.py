# Section 1.6.1

def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

sum_naturals(100)
# 5050

def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total

sum_cubes(100)
# 25502500

def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total
pi_sum(100)
# 3.1365926848388144

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x * x * x

def sum_cubes(n):
    return summation(n, cube)

result = sum_cubes(3)
# 36

def identity(x):
    return x

def sum_naturals(n):
    return summation(n, identity)

sum_naturals(10)
# 55

def square(x):
    return x * x

summation(10, square)
# 385

def pi_term(x):
    return 8 / ((4*x-3)*(4*x-1))

def pi_sum(n):
    return summation(n, pi_term)

pi_sum(1e6)
# 3.141592153589902

# Section 1.6.2

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

improve(golden_update, square_close_to_successor)
# 1.6180339887498951

from math import sqrt

phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation.'

improve_test()

# Section 1.6.3

def average(x, y):
    return (x + y) / 2

def sqrt_update(x, a):
    return average(x, a/x)

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)
sqrt(256)
# 16.0

# Section 1.6.4
