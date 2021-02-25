a_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(a_list):
    if a_list[i].isalpha() == False: #Проверяю на isalpha, т.к. isdigit не считает "+5" числом.
        if a_list[i][0] == '+' or a_list[i][0] == '-':
            a_list[i] = a_list[i].zfill(3)
        else:
            a_list[i] = a_list[i].zfill(2)
        a_list.insert(i, '"')
        a_list.insert(i + 2, '"')
        i += 4
    else:
        i += 1


print(a_list)

b_list = " ".join(a_list)
print(b_list)

#Получился слишком "костыльный" код и так и не понял как избавиться от пробелов при выводе.
#