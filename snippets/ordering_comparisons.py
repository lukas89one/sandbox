# Ordering Comparisons
# ---------------------------------------------------------------------------------------------------------------------

# Raise a TypeError exception when the operands don’t have a meaningful natural ordering

# print("[1, 2] > 'foo' = ", [1, 2] > 'foo')
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: '>' not supported between instances of 'list' and 'str'

# print("(1, 2) > 'foo' = ", (1, 2) > 'foo')
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: '>' not supported between instances of 'tuple' and 'str'

# print("[1, 2] > (1, 2) = ", [1, 2] > (1, 2))
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: '>' not supported between instances of 'list' and 'tuple'
# ---
# Python 2
#
# print "[1, 2] > 'foo' = ", [1, 2] > 'foo'
# [1, 2] > 'foo' =  False
#
# print "(1, 2) > 'foo' = ", (1, 2) > 'foo'
# (1, 2) > 'foo' =  True
#
# print "[1, 2] > (1, 2) = ", [1, 2] > (1, 2)
# [1, 2] > (1, 2) =  False

# ---------------------------------------------------------------------------------------------------------------------

# The cmp() function should be treated as gone, and the __cmp__() special method is no longer supported

# cmp(1, 2)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'cmp' is not defined

# a = 1
# a.__cmp__(2)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AttributeError: 'int' object has no attribute '__cmp__'

# ---
# Python 2
#
# cmp(1, 2)
# -1
#
# a = 1
# a.__cmp__(2)
# -1
# ---------------------------------------------------------------------------------------------------------------------
