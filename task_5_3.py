
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def tuple_create(tutors, klasses):
    tuple_list = (tuple(zip(tutors, klasses)))
    yield tuple_list

print(next(tuple_create(tutors, klasses)))

