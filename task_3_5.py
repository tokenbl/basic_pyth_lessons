import random #добавление библиотеки random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"] #заданы 3 списка из которых будут случайным образом
                                                                    #формироваться шутки
'''
Функция get_jokes(n), возвращающаю n шуток, сформированных из двух случайных слов, взятых из трёх списков:

'''

def get_jokes(n):
    jokes_list = []
    while n > 0:
        joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
        jokes_list.append(joke)
        n -= 1
    return jokes_list

print(get_jokes(4)) #вызов функции с заданным количеством шуток n

