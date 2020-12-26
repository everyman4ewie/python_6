# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
# (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго
# (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

# 1 вариант
from time import sleep  # выдает код с задержкой на определенное время в сек
from termcolor import colored  # импортирую цветное отображение вывода

class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый', 'желтый']

    def running(self):
        times = [4, 2, 4, 2]  # таймер светофора
        colors = [colored('Красный! Стой!', 'red'), colored('Желтый! Внимание!', 'yellow'), colored('Зеленый! Можно ехать!', 'green'), colored('Желтый! Внимание!', 'yellow')]
        while True:
            for i, el in enumerate(colors):
                print(colors[i].format(self.__color[i]))  # соответствующим элементам дается соответствующий тайминг
                sleep(times[colors.index(el)])
svetofor = TrafficLight()
svetofor.running()



# 2 вариант
# from time import sleep
#
# class TrafficLight:
#     def running(self):
#         while True:
#             print(colored('Красный', 'red'))
#             sleep(4)
#             print(colored('Желтый', 'yellow'))
#             sleep(1)
#             print(colored('Зеленый', 'green'))
#             sleep(4)
#             print(colored('Желтый', 'yellow'))
#             sleep(1)
#
# svetofor = TrafficLight()
# svetofor.running()
