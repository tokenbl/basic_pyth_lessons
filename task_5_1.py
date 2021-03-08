from random import randrange
from sys import argv

def odd_num(n):
    nums_gen = randrange(1, n + 1, 2)
    yield nums_gen

#if __name__ == '__main__':
     #n = argv[1]

print(*odd_num(100))