def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()

def reverse_string(s):
    return s[::-1]

import string_ops

print(string_ops.to_upper("hello"))
print(string_ops.to_lower("HELLO"))
print(string_ops.reverse_string("Python"))
