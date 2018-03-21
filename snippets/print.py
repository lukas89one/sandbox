# Print Is A Function
# ---------------------------------------------------------------------------------------------------------------------

# The print statement has been replaced with a print() function,
# with keyword arguments to replace most of the special syntax of the old print statement

print('Hello, World!')
# Hello, World!

print('some text,', end='')
print(' print more text on the same line')
# some text, print more text on the same line

print(('a', 'b'))  # tuple
# ('a', 'b')

print('a', 'b')  # multiple objects
# a b

print('There are <', 2**32, '> possibilities!', sep='')  # customize the separator between items
# There are <4294967296> possibilities!

# print 'Hello, World!'
#   File "<input>", line 1
#     print 'Hello, World!'
#                         ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Hello, World!')?

# ---
# Python 2
#
# print 'Hello, World!'
# Hello, World!
#
# print('Hello, World!')
# Hello, World!
#
# print "text", ; print 'print more text on the same line'
# text print more text on the same line
#
# Note: multiple objects => tuple
#
# print('a', 'b')
# ('a', 'b')
#
# print 'a', 'b'
# a b
# ---------------------------------------------------------------------------------------------------------------------
