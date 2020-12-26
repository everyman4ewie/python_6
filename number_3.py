# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

# 1 вариант (немного пошаманил)
from termcolor import colored

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._salary = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._salary.values())}'

    def get_total_incomes(self):
        return f'{0.87 * sum(self._salary.values())}'

pos_empl = ''
# Решил немного упростить процесс. Думал, конечно еще накрутить тут зависимость зарплаты
# всех сотрудников от количества продаж и количества продажников, но пока не понял как это сделать... Наверное нужно сделать через класс
number_employees = int(input('Сколько сотрудников в компании?'))
q = 1
while number_employees > q:
    name_employee = input('Введите имя сотрудника: ')
    surname_employee = input('Введите фамилию сотрудника: ')
    if pos_empl != '1' or pos_empl != '2' or pos_empl != '3' or pos_empl != '3' or pos_empl != '4' or pos_empl != '5' or pos_empl != '6':
        print(f'{pos_empl} - в нашей организации нет такой должности!')
    pos_empl = input('Какую должность занимает сотрудник? \n1 - Директор, \n2 - Заметитель директора, \n3 - Руководитель отдела, \n4 - Программист, \n5 - Бухгалтер, \n6 - Менеджер по продажам).\nВведите соответствующую цифру: ')
    if pos_empl == '1':
        position_employee = 'Директор'
        wage_employee = 600000
        bonus_employee = 0.4 * wage_employee
        q += 1
    elif pos_empl == '2':
        position_employee = 'Заместитель директора'
        wage_employee = 400000
        bonus_employee = 0.4 * wage_employee
        q += 1
    elif pos_empl == '3':
        position_employee = 'Руководитель отдела'
        wage_employee = 200000
        bonus_employee = 0.4 * wage_employee
        q += 1
    elif pos_empl == '4':
        position_employee = 'Программист'
        wage_employee = 100000
        bonus_employee = 0.4 * wage_employee
        q += 1
    elif pos_empl == '5':
        position_employee = 'Бухгалтер'
        wage_employee = 50000
        bonus_employee = 0.4 * wage_employee
        q += 1
    else:
        orders = int(input('Cколько сделок закрыл менеджер по продажам? Введите в штуках: '))
        order = orders * 25000
        position_employee = 'Менеджер по продажам'
        wage_employee = 10000
        bonus_employee = wage_employee + order
        q += 1
    my_worker = Position(name_employee, surname_employee, position_employee, wage_employee, bonus_employee)

    print(f'Имя сотрудника: {my_worker.get_full_name()}')
    print(f'Должность сотрудника: {my_worker.position}')
    print(f'Зарплата до уплаты налога: {my_worker.get_total_income()}\nЗарплата после уплаты налога: {my_worker.get_total_incomes()}')


# 2 вариант (то что просили сделать)
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._salary = {'wage': wage, 'bonus': bonus}
#
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return f'{self.name} {self.surname}'
#
#     def get_total_income(self):
#         return f'{sum(self._salary.values())}'
#
# my_worker = Position('Иван', 'Ячменьков', 'Программист', 70000, 80000)
#
# print(f'Имя сотрудника: {my_worker.get_full_name()}')
# print(f'Должность сотрудника: {my_worker.position}')
# print(f'Зарплата: {my_worker.get_total_income()}')
