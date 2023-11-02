# Section 1.2.1

42
# 42

-1 - -1
# 0

1/2 + 1/4 + 1/8 + 1/16 + 1/32 + 1/64 + 1/128
# 0.9921875

# Section 1.2.2
max(7.5, 9.5)
# 9.5

pow(100,2)
# 10000

pow(2,100)
# 1267650600228229401496703205376

max(1, -2, 3, -4)
# 3

max(min(1, -2), min(pow(3, 5), -4))
# -2

# Section 1.2.3
from math import sqrt
sqrt(256)
# 16.0

from operator import add, sub, mul

add(14, 28)
# 42
sub(100, mul(7, add(8, 4)))
# 16

# Section 1.2.4
radius = 10
radius
# 10
2 * radius
# 20
from math import pi
pi * 71 / 223
# 1.0002380197528042

max
# <built-in function max>

f = max
f(2, 3, 4)
# 4
f = 2
f
# 2

max = 5
max
# 5
max(2, 3, 4)
# TypeError: 'int' object is not callable
x = 2
x = x + 1
x
# 3

area, circumference = pi * radius * radius, 2 * pi * radius
area
# 314.1592653589793
circumference
# 62.83185307179586

radius = 11
area
# 314.1592653589793
area = pi * radius * radius
area
# 380.132711084365

x, y = 3, 4.5
y, x = x, y
x
# 4.5
y
# 3

# Section 1.2.5
sub(pow(2, add(1, 10)), pow(2, 5))
# 2016

add(x, 1)
# 5.5
x = 3

# Section 1.2.6
# Pure functions
abs(-2)
# 2

# Non-pure functions
print(1, 2, 3)
# 1 2 3

print(print(1), print(2))
# 1
# 2
# None None


