list_worker = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for worker in list_worker:
    worker = worker.split(' ')
    hello_worker = worker[-1].capitalize()
    print(f'Привет, {hello_worker}!')