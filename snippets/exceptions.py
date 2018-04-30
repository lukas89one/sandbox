# Changes To Exceptions
# ---------------------------------------------------------------------------------------------------------------------

# Raising exceptions. You must now use raise Exception(args) instead of raise Exception, args.

# raise IOError, "file error"
#   File "<input>", line 1
#     raise IOError, "file error"
#                  ^
# SyntaxError: invalid syntax

raise IOError("file error")
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# OSError: file error

# ---
# Python 2
#
# raise IOError, "file error"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IOError: file error
#
# raise IOError("file error")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IOError: file error
# ---------------------------------------------------------------------------------------------------------------------

# Catching exceptions. You must now use except SomeException as variable instead of except SomeException, variable.
# Moreover, the variable is explicitly deleted when the except block is left.

try:
    let_us_cause_a_NameError
except NameError as err:
    print(err, '--> our error message')
# name 'let_us_cause_a_NameError' is not defined --> our error message

# ---
# Python 2
#
# try:
#     let_us_cause_a_NameError
# except NameError, err:
#     print err, '--> our error message'
# name 'let_us_cause_a_NameError' is not defined --> our error message
# ---------------------------------------------------------------------------------------------------------------------

# Exception chaining. There are two cases: implicit chaining and explicit chaining
# Implicit chaining happens when an exception is raised in an except or finally handler block.

try:
    let_us_cause_a_NameError
except NameError as err:
    let_us_cause_a_SecondNameError
    print(err, '--> our error message')

# Traceback (most recent call last):
#   File "<input>", line 2, in <module>
# NameError: name 'let_us_cause_a_NameError' is not defined
# During handling of the above exception, another exception occurred:
# Traceback (most recent call last):
#   File "<input>", line 4, in <module>
# NameError: name 'let_us_cause_a_SecondNameError' is not defined

# Explicit chaining is invoked with this syntax: raise SecondaryException() from primary_exception

raise Exception('second') from Exception('first')

# Exception: first
# The above exception was the direct cause of the following exception:
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# Exception: second

# ---
# Python 2
#
# try:
#     let_us_cause_a_NameError
# except NameError as err:
#     let_us_cause_a_SecondNameError
#     print(err, '--> our error message')
# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# NameError: name 'let_us_cause_a_SecondNameError' is not defined

# Suppressing exception context

try:
    let_us_cause_a_NameError
except NameError as err:
    try:
        let_us_cause_a_SecondNameError
        print(err, '--> our error message')
    except NameError as err:
        raise Exception('SecondNameError')
# Traceback (most recent call last):
#   File "<input>", line 2, in <module>
# NameError: name 'let_us_cause_a_NameError' is not defined
# During handling of the above exception, another exception occurred:
# Traceback (most recent call last):
#   File "<input>", line 5, in <module>
# NameError: name 'let_us_cause_a_SecondNameError' is not defined
# During handling of the above exception, another exception occurred:
# Traceback (most recent call last):
#   File "<input>", line 8, in <module>
# Exception: SecondNameError

try:
    let_us_cause_a_NameError
except NameError as err:
    try:
        let_us_cause_a_SecondNameError
        print(err, '--> our error message')
    except NameError as err:
        raise Exception('SecondNameError') from None
# Traceback (most recent call last):
#   File "<input>", line 8, in <module>
# Exception: SecondNameError
# ---------------------------------------------------------------------------------------------------------------------

# Exception objects now store their traceback as the __traceback__ attribute

try:
    let_us_cause_a_NameError
except NameError as err:
    print(type(err.__traceback__))

# <class 'traceback'>
# ---------------------------------------------------------------------------------------------------------------------
