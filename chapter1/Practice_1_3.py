# Section 1.3

def square(x):
    return mul(x, x)

square(21)
# 441

square(add(2, 5))
# 49

square(square(3))
# 81

def sum_squares(x, y):
    return add(square(x), square(y))

sum_squares(3, 4)
# 25

def g():
    return 1

g()
# 1

g = 2
g
# 2

def g(h, i):
    return h + i

g(1, 2)
# 3

# Section 1.3.1

from math import pi

tau = 2 * pi

from operator import mul

def square(x):
    return mul(x, x)

f = max
max = 3
result = f(2, 3, 4)
max(1, 2)
# TypeError: 'int' object is not callable

# Section 1.3.2
from operator import mul

def square(x):
    return mul(x, x)

square(-2)
# 4

# Section 1.3.3
from math import add, mul
def square(x):
    return mul(x, x)

def sum_squares(x, y):
    return add(square(x), square(y))

result = sum_squares(5, 12)
result
# 169

# Section 1.3.4

def square(x):
    return mul(x, x)

def square(y):
    return mul(y, y)

# Section 1.3.5
# Section 1.3.6

def square(x):
    return mul(x, x)

def square(x):
    return mul(x, x-1) + x

# Section 1.3.7
2 + 3
# 5

add(2, 3)
# 5

2 + 3 * 4 + 5
# 19

(2 + 3) * (4 + 5)
# 45

# equivalent to 2 + 3 * 4 + 5 in mul and add
mul(add(2, 3), add(4, 5))
# 45

5 / 4
# 1.25

8 / 4
# 2.0

5 // 4
# 1

8 // 4
# 2

5 // 4
# 1

-5 // 4
# -2

from operator import floordiv, truediv

truediv(5, 4)
# 1.25

floordiv(5, 4)
# 1



