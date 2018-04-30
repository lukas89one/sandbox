# Builtins
# ---------------------------------------------------------------------------------------------------------------------

# New super(). You can now invoke super() without arguments and (assuming this is in a regular instance method defined
# inside a class statement) the right class and instance will automatically be chosen


class P(object):
    def a(self):
        print('P')


class C(P):
    def a(self):
        print('C')

    def p_a(self):
        super().a()


c = C()
c.a()
c.p_a()
# C
# P

# ---
# Python 2
#
# class P(object):
#     def a(self):
#         print('P')
#
# class C(P):
#     def a(self):
#         print('C')
#     def p_a(self):
#         super(C, self).a()
#
# c = C()
# c.a()
# c.p_a()
# C
# P
# ---------------------------------------------------------------------------------------------------------------------

# raw_input() was renamed to input().
# That is, the new input() function reads a line from sys.stdin and returns it with the trailing newline stripped

my_input = input('enter a number: ')
# enter a number: 123
type(my_input)
# <class 'str'>

# ---
# Python 2
#
# my_input = input('enter a number: ')
#
# enter a number: 123
#
# type(my_input)
# <type 'int'>
#
# my_input = raw_input('enter a number: ')
# enter a number: 123
#
# type(my_input)
# <type 'str'>
# ---------------------------------------------------------------------------------------------------------------------

# A new built-in function next() was added to call the __next__() method on an object

my_generator = (letter for letter in 'abcdefg')
next(my_generator)
'a'

# my_generator.next()
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AttributeError: 'generator' object has no attribute 'next'

# ---
# Python 2
#
# my_generator = (letter for letter in 'abcdefg')
# next(my_generator)
# 'a'
# my_generator.next()
# 'b'
# ---------------------------------------------------------------------------------------------------------------------

# The round() function rounding strategy and return type have changed.
# Exact halfway cases are now rounded to the nearest even result instead of away from zero.
# It generally returns an integer when called with a single argument and a value of the same type as x when called
# with two arguments.

round(15.5)
# 16

round(16.5)
# 16

# ---
# Python 2
#
# round(15.5)
# 16.0
#
# round(16.5)
# 17.0
# ---------------------------------------------------------------------------------------------------------------------
