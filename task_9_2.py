class Road:

    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width
        self.weight = 25
        self.height = 5


    def all_road(self):
        all_road = self._length * self._width * self.weight * self.height / 1000
        print('Масса асфальта, необходимого для покрытия всей дороги = ', (all_road),'тонн.')

a = Road(5000, 20)
a.all_road()