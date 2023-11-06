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