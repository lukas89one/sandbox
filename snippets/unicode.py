# Unicode
# ---------------------------------------------------------------------------------------------------------------------

# Everything you thought you knew about binary data and Unicode has changed

print('Python 3 strings are now utf-8 \u03BCnico\u0394é!')
# strings are now utf-8 μnicoΔé!

print('Python 3 has', type(b' bytes for storing data'))
# Python 3 has <class 'bytes'>

print('Python 3 also has', type(bytearray(b'bytearrays')))
# and Python 3 also has <class 'bytearray'>

# 'note that we cannot add a string' + b'bytes for data'
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: must be str, not bytes

# ---
# Python 2
#
# print type(unicode('this is like a python3 str type'))
# <type 'unicode'>
#
# print type(b'byte type does not exist')
# <type 'str'>
#
# print 'they are really' + b' the same'
# they are really the same
#
# print type(bytearray(b'bytearray oddly does exist though'))
# <type 'bytearray'>
# ---------------------------------------------------------------------------------------------------------------------
