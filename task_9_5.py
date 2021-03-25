class Stationery:
    def __init__(self, title='stationery'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')

class Marker(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')

a = Stationery()
a.draw()
pen = Pen()
pen.draw()
penc = Pencil()
penc.draw()
mar = Marker()
mar.draw()
