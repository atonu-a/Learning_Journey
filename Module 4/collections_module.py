from collections import Counter, defaultdict

# print(__doc__)

fruits = ['apple', 'banana', 'orange', 'apple', 'bean']

print(Counter(fruits))
print(Counter(fruits).most_common(2))

word_dict = defaultdict(list) # values will be as a list

word_dict['python'].append("Programming Language")
word_dict['python'].append("A Snake")
word_dict['apple'].append("Fruit")
word_dict['Atonu'].append('name')
print(word_dict)    #defaultdict(<class 'list'>, {'python': ['Programming Language', 'A Snake'], 'apple': ['Fruit'], 'Atonu': ['name']})