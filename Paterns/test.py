import copy

e = [[1, 2],[4, 5, 6],[7, 8, 9]]

e1 = copy.copy(e)
e2 = copy.deepcopy(e)

e[0].append(3)
e.append([10, 11, 12])

print(e)
print(e1)
print(e2)


