data_nums = {'zero': 'ноль',
             'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',
             'ten': 'десять'}


def num_translate(num):
    for items in data_nums:
        if num == items:
            return data_nums.get(items) #функция возвращает перевод числительного или None,
                                        #если такого числительного нет в словаре

print(num_translate('five')) #вызываем функцию, в качестве аргумента указываем на английском числительное от 0 до 10
print(num_translate('eleven')) #вызываем функцию, в качестве аргумента указываем числительное, которого нет в словаре