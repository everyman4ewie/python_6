
class Stationery:
    def __init__(self, title="Начинаю рисовать!"):
        self.title = title
    def draw(self):
        print(f'{self.title}')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Рисую {self.title} ручкой.')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Рисую {self.title} карандашом.')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Рисую {self.title} маркером.')

my_stat = Stationery()
my_stat.draw()
pen = Pen('гелевой')
pen.draw()
pencil = Pencil('черным')
pencil.draw()
handle = Handle('красным')
handle.draw()