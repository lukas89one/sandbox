# Removed Syntax
# ---------------------------------------------------------------------------------------------------------------------

#  Tuple parameter unpacking removed

# def f(a, (b, c)):
#     print(a, b, c)

#   File "<input>", line 1
#     def f(a, (b, c)):
#              ^
# SyntaxError: invalid syntax


def f(a, b_c):
    b, c = b_c
    print(a, b, c)


f(1, (2, 3))
# 1 2 3

# ---
# Python 2
#
# def f(a, (b, c)):
#     print a, b, c
#
# f(1, (2, 3))
#
# 1 2 3
# ---------------------------------------------------------------------------------------------------------------------

# Removed <>

1 != 2
# True

# 1 <> 2
#   File "<input>", line 1
#     1 <> 2
#        ^
# SyntaxError: invalid syntax

# ---
# Python 2
#
# 1 != 2
# True
#
# 1 <> 2
# True
# ---------------------------------------------------------------------------------------------------------------------

# The from module import * syntax is only allowed at the module level, no longer inside functions

# def f():
#     from datetime import *

#   File "<input>", line 1
# SyntaxError: import * only allowed at module level

# ---
# Python 2
#
# def f():
#     from datetime import *
#
# <stdin>:1: SyntaxWarning: import * only allowed at module level
# ---------------------------------------------------------------------------------------------------------------------
