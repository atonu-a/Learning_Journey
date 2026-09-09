a = [1, 2, 3, 4, 5, 6]

# Normal way
reuslt = []
for i in a:
    if i%2==0:
        reuslt.append(i**2)
    else:
        reuslt.append(i)
print(reuslt)

# Comprehension way
reuslt_new = [i**2 if i%2==0 else i for i in a]
print(reuslt_new)

new_result = [i for i in a if i%2==0]
print(new_result)

