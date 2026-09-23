# Module / packeges importing
import calc #everything imported
# from calc import * # the worst way
print(calc.add(5, 7))
print(calc.sub(5, 7))

from calc import sub #Only sub has been imported

print(sub(5, 7))