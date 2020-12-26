# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать
# формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число
# см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

# 1 вариант (немного добавил параметров и все)
class Road:
    def __init__(self, length=5000, width=20, thickness=5, quality=25):
        self._length = length  # длина дороги
        self._width = width  # ширина дороги
        self._thickness = thickness  # толщина дорожного полотна
        self._quality = quality  # качество асфальта

    def building_road(self):
        return f'{self._length}м * {self._width}м * 25кг * 5см = {self._length * self._width * self._quality * self._thickness / 1000}т'
while True:
    i = input('Вы хотите изменить толщину асфальта? (Стандартная толщина 5 см) ') == 'да'
    j = input('Вы хотите изменить количество асфальта? (Стандартное количество 25 кг/мˆ2) ') == 'да'
    try:
        l = int(input('Введите длину трассы в м: '))
        w = int(input('Введите ширину трассы в м: '))
        if i == 'да':
            t = int(input('Введите необходимую толщину асфальта в см: '))
        else:
            t = 5
        if j == 'да':
            q = int(input('Введите количество асфальта в кг: '))
        else:
            q = 25
    except ValueError:
        print('Вы ввели параметры дороги не в цифрах! Попробуйте еще раз!')
    else:
        my_road = Road(l, w, t, q)
        print(my_road.building_road())
        break



# 2 вариант (то что просили сделать)
# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def building_road(self):
#         return f'{self._length}м * {self._width}м * 25кг * 5см = {self._length * self._width * 25 * 5 / 1000}т'
# while True:
#     try:
#         l = int(input('Введите длину трассы в м: '))
#         w = int(input('Введите ширину трассы в м: '))
#     except ValueError:
#         print('Вы ввели параметры дороги не в цифрах! Попробуйте еще раз!')
#     else:
#         my_road = Road(l, w)
#         print(my_road.building_road())
#         break
