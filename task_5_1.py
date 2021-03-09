from random import randrange

def odd_nums(n):
    nums_gen = randrange(1, n + 1, 2)
    yield nums_gen

odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))
