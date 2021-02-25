price_list = [11.24, 90.78, 13.71, 42.52, 57, 71, 85.10, 12.11, 9.41, 35.07, 3.54, 98.20,
              42.40, 59, 6.05, 99.9, 12, 2.30, 4.50]
print(id(price_list)) #вывод id для сравнения со списком в #B
#A
for price in price_list:
    rub = int(price)
    kop = abs(round((rub - price) * 100))
    print(f'{rub} руб {kop:02} коп', end = ', ')

#B
price_list.sort()
print(price_list)

print(id(price_list)) #Вывод id списка в начале и в конце доказывает, что новый список не создавался(?)

#C
sorted_price_list = sorted(price_list, reverse = True)
print(sorted_price_list) #Создался новый список

#D
print(sorted(sorted_price_list[:5], reverse = False))
