import functools

list1 = [{1, 2, 3, 4, 5, 6, 7}, {2, 4, 6, 8, 10}, {10, 2, 3, 1, 5}]
result = functools.reduce(lambda x, y: x | y, list1)
print(result)