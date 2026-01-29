import copy

a = ([1,2],[4,5])
b = copy.deepcopy(a)

b[0].append(44)

print(a)
print(b)



