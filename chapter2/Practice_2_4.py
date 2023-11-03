# Section 2.4.1
print("\nSection 2.4.1")
from datetime import date

tues = date(2014, 5, 13)
print(date(2014, 5, 19) - tues)
# 6 days, 0:00:00
print("tues.year\n # ", tues.year)
# 2014

tues.strftime("%A %B %d")
# 'Tuesday May 13'

print("'1234'.isnumeric()\n # ", '1234'.isnumeric())
# True

print("'rOBERT dE nIRO'.swapcase()\n # ", 'rOBERT dE nIRO'.swapcase())
# 'Robert De Niro'

print("'eyes'.upper().endswith('YES')\n # ", 'eyes'.upper().endswith('YES'))
# True

print("\nSection 2.4.2")

chinese = ['coin', 'string', 'myriad']
suits = chinese
print("suits.pop()\n # ", suits.pop())
# 'myriad'

suits.remove('string')
# suits
# ['coin']

suits.append('cup')
# suits
# ['coin', 'cup']
suits.extend(['sword', 'club'])
# suits
# ['coin', 'cup', 'sword', 'club']
suits[2] = 'spade'
# suits
# ['coin', 'cup', 'spade', 'club']
suits[0:2] = ['heart', 'diamond']
# suits
# ['heart', 'diamond', 'spade', 'club']

print("chinese\n # ", chinese)
# ['heart', 'diamond', 'spade', 'club']

nest = list(suits)
nest[0] = suits

nest[0].insert(2, 'Joker')
print("nest\n # ", nest)
# [['heart', 'diamond', 'Joker', 'spade', 'club'], 'diamond', 'spade', 'club']

nest[0].pop(2)
# 'Joker'
suits
# ['heart', 'diamond', 'spade', 'club']

suits is nest[0]
# True

suits is ['heart', 'diamond', 'spade', 'club']
# False

suits == ['heart', 'diamond', 'spade', 'club']
# True

print("List comprehensions")

from unicodedata import lookup

[lookup('WHITE ' + s.upper() + ' SUIT') for s in suits]
# ['♡', '♢', '♤', '♧']

print("Tuples")

1, 2 + 3
# (1, 5)

("the", 1, ("and", "only"))
# ('the', 1, ('and', 'only'))
type((10, 20))
# <class 'tuple'>

() # 0 elements
# ()

# Note how 1 element tuples are defined:
# we need a comma after the element.
(10,) # 1 element
# (10,)

print("(10,)\n # ", (10,)) # 1 element

(10) # just an integer
# 10

print("(10)\n # ", (10)) # just an integer

code = ("up", "up", "down", "down") + ("left", "right") * 2
len(code)
# 8

code[3]
# 'down'

code.count("down")
# 2

code.index("left")
# 4

print("\nSection 2.4.3")
numerals = {'I': 1.0, 'V': 5, 'X': 10}
numerals['X']
# 10


# we can update the value associated with a key
numerals['I'] = 1

# or add a new key-value pair
numerals['L'] = 50

numerals
# {'I': 1, 'V': 5, 'X': 10, 'L': 50}

sum(numerals.values())
# 66

dict([(3, 9), (4, 16), (5, 25)])
# {3: 9, 4: 16, 5: 25}

# call get with a key that doesn't exist
numerals.get('A', 0)
# 0

# call get with a key that does exist
numerals.get('V', 0)
# 5

print("\nSection 2.4.4")

# We wish to write a withdraw function that simulates an account with $100.00
# balance. Each call to withdraw(amount) should deduct the amount from the
# balance, as long as sufficient funds are available. If funds are insufficient,

# withdrawals(25)
# # 75
# withdrawals(25)
# # 50
# withdrawals(60)
# # 'Insufficient funds'
# withdrawals(15)
# # 35

# withdrawals = make_withdraw(100)

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance            # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount  # Rebind the existing balance name
        return balance
    return withdraw

withdrawals = make_withdraw(100)
withdrawals(25)
# 75
withdrawals(25)
# 50
withdrawals(60)
# 'Insufficient funds'
withdrawals(15)
# 35

print("\nSection 2.4.5")

print("\nSection 2.4.6")

print("\nSection 2.4.7")

# sample pseudo code only, not a working code. It's here
# to illustrate the idea of a functional implementation of link.

# def mutable_link():
#     """Return a functional implementation of a mutable linked list."""
#     contents = empty
#     def dispatch(message, value=None):
#         nonlocal contents
#         if message == 'len':
#             return len_link(contents)
#         elif message == 'getitem':
#             return getitem_link(contents, value)
#         elif message == 'push_first':
#             contents = link(value, contents)
#         elif message == 'pop_first':
#             f = first(contents)
#             contents = rest(contents)
#             return f
#         elif message == 'str':
#             return join_link(contents, ", ")
#     return dispatch

# def to_mutable_link(source):
#     """Return a functional list with the same contents as source."""
#     s = mutable_link()
#     for element in reversed(source):
#         s('push_first', element)
#     return s

print("\nSection 2.4.8")

def account(initial_balance):
	    def deposit(amount):
	        dispatch['balance'] += amount
	        return dispatch['balance']
	    def withdraw(amount):
	        if amount > dispatch['balance']:
	            return 'Insufficient funds'
	        dispatch['balance'] -= amount
	        return dispatch['balance']
	    dispatch = {'deposit':   deposit,
	                'withdraw':  withdraw,
	                'balance':   initial_balance}
	    return dispatch
	
def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)
def check_balance(account):   	    
    return account['balance']
   	
a = account(20)
deposit(a, 5)
# 25
withdraw(a, 17)
# 8
check_balance(a)
# 8
