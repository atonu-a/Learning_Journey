#  {}
# Unordered --> indexing is not supported
# immutable --> no update
# set() method


"""a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 3, 1, 2]
print(a)
s = set(a)
print(s)"""

a = {1, 2, 3}
b = {2, 3, 4}

c = a.union(b)
d = a.intersection(b)
e = b.intersection(a)
f = b.union(a)
print(c)
print(d)
print(e)
print(f)
