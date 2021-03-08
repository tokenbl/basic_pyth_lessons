
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_items = [item for ind, item in enumerate(src) if item > src[ind - 1] and ind > 0]
print('result =', list_items)

