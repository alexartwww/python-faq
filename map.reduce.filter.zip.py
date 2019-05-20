from functools import reduce

a = list(range(10))
b = list(range(12))[::-1]
print(list(zip(a, b)))
print(list(map(lambda i, j: (i, j), a, b)))
print(list(filter(lambda i: i > 5, a)))
print(list(reduce(lambda i: i, a)))


