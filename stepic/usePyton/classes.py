
"""
class Buffer:
    capacity = 0
    count = 0
    print = 5
    mas = []
    def __init__(self):
        capacity = 0
        count = 0
        print = 5
        mas = []
        # конструктор без аргументов

    def add(self, *a):
        self.mas.extend(a)
        self.capacity += len(a)
        # печать суммы массива
        def sumir(*ma):
            sum_ma = 0
            for i in ma:
                sum_ma += i
            print(sum_ma)

        while self.capacity > 4:
            sums = 0
            sums += self.mas.pop(0)
            sums += self.mas.pop(0)
            sums += self.mas.pop(0)
            sums += self.mas.pop(0)
            sums += self.mas.pop(0)
            print(sums)
            self.capacity -= 5
        # добавить следующую часть последовательности

    def get_current_part(self):
        return self.mas[0 : self.capacity]
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
"""

class Buffer:
    mas = []
    def __init__(self):
        mas = []
        # конструктор без аргументов

    def add(self, *a):
        self.mas.extend(a)
        while len(self.mas) > 4:
            print(sum(self.mas[:5]))
            self.mas = self.mas[5:]
        # добавить следующую часть последовательности

    def get_current_part(self):
        return self.mas[0 : len(self.mas)]
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены

buf = Buffer()
buf.add(1, 2, 3)
part = buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
part = buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
part = buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
part = buf.get_current_part() # вернуть [1]





"""
class MoneyBox:
    capacity = 0
    count = 0
    def __init__(self, capacity):
        self.capacity = capacity
        count = 0
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if v <= self.capacity - self.count:
            return True
        else:
            return False
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        self.count += v
        # положить v монет в копилку
"""