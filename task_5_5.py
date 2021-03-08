
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

#решение "в лоб":
uniq_items = [item for item in src if src.count(item) == 1]
print('result =', uniq_items)

#попытка оптимизировать:
uniq_items = [item for item in src if item in uniq_items]
print('result =', uniq_items)