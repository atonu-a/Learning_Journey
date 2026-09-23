# # Module / packeges importing
# import calc #everything imported
# # from calc import * # the worst way
# print(calc.add(5, 7))
# print(calc.sub(5, 7))

# from calc import sub #Only sub has been imported

# print(sub(5, 7))

from mathmatics.calculator import add, sub, mul, div
from mathmatics import xyz #imported from __init__.py

print(add(5,5))
print(sub(5,5))
print(mul(5,5))
print(div(5,5))
print(xyz)