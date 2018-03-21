# Views And Iterators Instead Of Lists
# ---------------------------------------------------------------------------------------------------------------------

# range() now behaves like xrange() used to behave, except it works with values of arbitrary size

print(range(10))
# range(0, 10)

print(type(range(10)))
# <class 'range'>

print(list(range(10)))  # If we need a list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(xrange(10))
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'xrange' is not defined

# ---
# Python 2
#
# print(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(type(range(10)))
# <type 'list'>
#
# print(xrange(10))
# xrange(10)
#
# print(type(xrange(10)))
# <type 'xrange'>
# ---------------------------------------------------------------------------------------------------------------------

# dict methods dict.keys(), dict.items() and dict.values() return “views” instead of lists

d = {'a': 1}
type(d.keys())
# <class 'dict_keys'>

type(d.items())
# <class 'dict_items'>

type(d.values())
# <class 'dict_values'>

# ---
# Python 2
#
# dict methods dict.keys(), dict.items() and dict.values() return lists
# d = {'a': 1}
# type(d.keys())
# <type 'list'>
#
# type(d.items())
# <type 'list'>
#
# type(d.values())
# <type 'list'>
# ---------------------------------------------------------------------------------------------------------------------

# dict.iterkeys(), dict.iteritems() and dict.itervalues() methods are no longer supported

# type(d.iterkeys())
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'iterkeys'
#
# type(d.iteritems())
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'iteritems'
#
# type(d.itervalues())
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'itervalues'

# ---
# Python 2
#
#
# type(d.iterkeys())
# <type 'dictionary-keyiterator'>
#
# type(d.iteritems())
# <type 'dictionary-itemiterator'>
#
# type(d.itervalues())
# <type 'dictionary-valueiterator'>
# ---------------------------------------------------------------------------------------------------------------------

# map(), filter() and zip() return iterators

map(lambda v: d[v], d)
# <map object at 0x7f8caed93f60>

filter(lambda v: v == 1, d.values())
# <filter object at 0x7f8caed93f60>

zip(d.values())
# <zip object at 0x7f8caf058448>

# ---
# Python 2
#
# map(lambda v: d[v], d)
# [1]

# filter(lambda v: v == 1, d.values())
# [1]

# zip(d.values())
# [(1,)]
# ---------------------------------------------------------------------------------------------------------------------
