s = '   immutable   '
# we CANNOT alter members of a string
# s[0] = 'I' # fails
n = s.strip()
S = n.capitalize()
print(S)

# ref or value
a = 1
b = a
a = 2
print(a,b) # simple variables use VALUE
m = [7,6,5]
n = m # by REFERENCE - they both refer to the same thing
m[0] = 'changed'
print(m,n)