# Changed Syntax
# ---------------------------------------------------------------------------------------------------------------------

# New Metaclass Syntax


class M(type):
    pass


class C(metaclass=M):
    pass

# ---
# Python 2
#
# class M(type):
#     pass
#
#
# class C:
#     __metaclass__ = M
#     pass
# ---------------------------------------------------------------------------------------------------------------------

# List comprehensions no longer support the syntactic form [... for var in item1, item2, ...].
# Use [... for var in (item1, item2, ...)] instead.

[i for i in (1, 2, 3)]
# [1, 2, 3]

# ---
# Python 2
#
# [i for i in 1, 2, 3]
# [1, 2, 3]

# For-loop variables and the global namespace leak

i = 'a'
print(i)
print([i for i in range(5)])
print(i)
# a
# [0, 1, 2, 3, 4]
# a


# ---
# Python 2
#
# i = 'a'
# print i
# print [i for i in range(5)]
# print i
#
# a
# [0, 1, 2, 3, 4]
# 4
# ---------------------------------------------------------------------------------------------------------------------
