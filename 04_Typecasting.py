# Variable declarations with different data types
a = 50         # Integer
b = 7.99       # Float
c = 50.55      # Float
d = "59"       # String (number in string format)
e = "hello"    # String (non-numeric)
f = ""         # Empty string
g = True       # Boolean (True)
h = False      # Boolean (False)

# Converting to int
print(int(a))   # Converts integer to int (no change)
print(int(b))   # Converts float to int (truncates decimal part)
print(int(c))   # Converts float to int (truncates decimal part)
print(int(d))   # Converts numeric string to int
# print(int(e)) # Error: cannot convert non-numeric string to int
# print(int(f)) # Error: cannot convert empty string to int
print(int(g))   # Converts True to 1 (True is equivalent to 1 in Python)
print(int(h))   # Converts False to 0 (False is equivalent to 0 in Python)

# Converting to float
print(float(a))  # Converts integer to float
print(float(b))  # No change (already a float)
print(float(c))  # No change (already a float)
print(float(d))  # Converts numeric string to float
# print(float(e)) # Error: cannot convert non-numeric string to float
# print(float(f)) # Error: cannot convert empty string to float
print(float(g))  # Converts True to 1.0
print(float(h))  # Converts False to 0.0

# Converting to string
print(str(a))  # Converts integer to string
print(str(b))  # Converts float to string
print(str(c))  # Converts float to string
print(str(d))  # No change (already a string)
print(str(e))  # No change (already a string)
print(str(f))  # No change (already a string, just empty)
print(str(g))  # Converts True to "True"
print(str(h))  # Converts False to "False"

# Converting to boolean
print(bool(a))  # Any non-zero number is True (50 -> True)
print(bool(b))  # Any non-zero float is True (7.99 -> True)
print(bool(c))  # Any non-zero float is True (50.55 -> True)
print(bool(d))  # Any non-empty string is True ("59" -> True)
print(bool(e))  # Any non-empty string is True ("hello" -> True)
print(bool(f))  # Empty string is False ("" -> False)
print(bool(g))  # True remains True
print(bool(h))  # False remains False
