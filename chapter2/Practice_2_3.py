print("\nSection 2.3.1")
digits = [1, 8, 2, 8]
print("len(digits)\n #", len(digits))
print("digits[3]\n #", digits[3])

print("[2, 7] + digits * 2\n #", [2, 7] + digits * 2)
pairs = [[10, 20], [30, 40]]
print("pairs[1]\n# ", pairs[1])
print("pairs[1][0]\n #", pairs[1][0])

print("\nSection 2.3.2")


def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total


print("count(digits, 8)\n #", count(digits, 8))


def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total


print("count(digits, 8)\n #", count(digits, 8))

pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
same_count = 0
for x, y in pairs:
    if x == y:
        same_count = same_count + 1
print("same_count\n #", same_count)

range(1, 10)  # Includes 1, but not 10
print("range(1, 10)\n #", range(1, 10))
print("list(range(5, 8))\n #", list(range(5, 8)))
print("list(range(4))\n #", list(range(4)))

for _ in range(3):
    print('Go Bears!')

print("\nSection 2.3.3")
odds = [1, 3, 5, 7, 9]
print("[x+1 for x in odds]\n", [x + 1 for x in odds])
print("[x for x in odds if 25 % x == 0]\n #", [x for x in odds if 25 % x == 0])


def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]


print("divisors(4)\n #", divisors(4))
print("divisors(12)\n #", divisors(12))

print("[n for n in range(1, 1000) if sum(divisors(n)) == n]\n #",
      [n for n in range(1, 1000) if sum(divisors(n)) == n])


def width(area, height):
    assert area % height == 0
    return area // height


def perimeter(width, height):
    return 2 * width + 2 * height


def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)


area = 80
print("width(area, 5)\n #", width(area, 5))
print("perimeter(16, 5)\n #", perimeter(16, 5))
print("perimeter(10, 8)\n #", perimeter(10, 8))
print("minimum_perimeter(area)\n #", minimum_perimeter(area))


def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]


def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]


def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced


from operator import mul
print("reduce(mul, [2, 4, 8], 1)\n #", reduce(mul, [2, 4, 8], 1))


def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))


print("divisors_of(12)\n #", divisors_of(12))

from operator import add


def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)


def perfect(n):
    return sum_of_divisors(n) == n


print("keep_if(perfect, range(1, 1000))\n #",
       keep_if(perfect, range(1, 1000)))

# Conventional names for higher-order functions
apply_to_all = lambda map_fn, s: list(map(map_fn, s))
keep_if = lambda filter_fn, s: list(filter(filter_fn, s))

from functools import reduce
from operator import mul


def product(s):
    return reduce(mul, s)


print("product([1, 2, 3, 4, 5])\n #",
      product([1, 2, 3, 4, 5]))

print("\nSection 2.3.4")
print("digits\n #", digits)
# [1, 8, 2, 8]

print("2 in digits\n #", 2 in digits)
# True

print("1828 not in digits\n #", 1828 not in digits)
# True

print("digits[0:2]\n #", digits[0:2])
# [1, 8]

print("digits[1:]\n #", digits[1:])
# [8, 2, 8]
print("\nSection 2.3.5")

print("'I am string!'\n# ", 'I am string!')
# I am string!
print("I've got an apostrophe")
# I've got an apostrophe
print("'您好'\n# ", '您好')
# 您好

city = 'Berkeley'
print("len(city)\n #", len(city))
# 8
print("city[3]\n #", city[3])
# k
print("'Berkeley' + ', CA'\n#", 'Berkeley' + ', CA')
# Berkeley, CA

print("'Shabu ' * 2\n# ", 'Shabu ' * 2)
# Shabu Shabu

print("'here' in \"Where's Waldo?\"\n #", 'here' in "Where's Waldo?")
# True
my_str = """The Zen of Python
claims, Readability counts.
Read more: import this."""

print("my_str\n #", my_str)
# The Zen of Python
# claims, Readability counts.
# Read more: import this.

print("str(2) + ' is an element of ' + str(digits)\n #", str(2) + ' is an element of ' + str(digits))
# 2 is an element of [1, 8, 2, 8]



print("\nSection 2.3.6")


def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)


def label(tree):
    return tree[0]

    
def branches(tree):
    if isinstance(tree, list) and len(tree) > 1:
        return tree[1:]
    else:
        return []


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)

        
t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print("t\n #", t)
label(t)
print("label(t)\n #", label(t))

print("label(branches(t)[1])\n #", label(branches(t)[1]))
print("is_leaf(t)\n #", is_leaf(t))

print("is_leaf(branches(t)[0]\n #", is_leaf(branches(t)[0]))


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


print("fib_tree(5)\n #", fib_tree(5))


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)


print("count_leaves(fib_tree(5))\n #", count_leaves(fib_tree(5)))


def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])


print("partition_tree(2, 2)\n #", partition_tree(2, 2))


def right_binarize(tree):
        """Construct a right-branching binary tree."""
        if is_leaf(tree):
            return tree
        if len(tree) > 2:
            tree = [tree[0], tree[1:]]
        return [right_binarize(b) for b in tree]

        
print("right_binarize([1, 2, 3, 4, 5, 6, 7])\n #", right_binarize([1, 2, 3, 4, 5, 6, 7]))

print("\nSection 2.3.7")

empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]


four = link(1, link(2, link(3, link(4, empty))))
print("four\n #", four)
first(four)
print("first(four)\n #", first(four))
print("rest(four)\n #", rest(four))


def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


print("len_link(four)\n #", len_link(four))

print("getitem_link(four, 1)\n #", getitem_link(four, 1))


def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))


def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)


print("len_link_recursive(four)\n #", len_link_recursive(four))

print("getitem_link_recursive(four, 1)\n #", getitem_link_recursive(four, 1))


def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))


print("extend_link(four, four)\n# ", extend_link(four, four))


def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


print("apply_to_all_link(lambda x: x*x, four)\n #", apply_to_all_link(lambda x: x * x, four))
# [1, [4, [9, [16, 'empty']]]]


def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept


print("keep_if_link(lambda x: x%2 == 0, four)\n #", keep_if_link(lambda x: x % 2 == 0, four))


def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)


print("join_link(four, ", ")\n #", join_link(four, ", "))
# 1, 2, 3, 4


def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty)  # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n - m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m - 1)
        return extend_link(with_m, without_m)

        
def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))


print("print_partitions(6, 4)")
print_partitions(6, 4)
