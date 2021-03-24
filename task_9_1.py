from time import sleep
from termcolor import colored


class TrafficLight:
    __color__ = 'Красный', 'Желтый', 'Зелёный'

    def running(self):
        num_color = 0
        if num_color == 0:
            print(colored(TrafficLight.__color__[num_color], 'red'))
            sleep(7)
            num_color += 1
        if num_color == 1:
            print(colored(TrafficLight.__color__[num_color], 'yellow'))
            sleep(2)
            num_color += 1
        if num_color == 2:
            print(colored(TrafficLight.__color__[num_color], 'green'))
            sleep(6)
            num_color += 1


a = TrafficLight()
a.running()
