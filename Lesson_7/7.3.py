# task3
# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке
# https://pythonworld.ru/osnovy/peregruzka-operatorov.html

# class Cell:
#     def __init__(self, quantity):
#         self.quantity = int(quantity)
#
#     def __str__(self):
#         return f'Результат операции {self.quantity * "*"}'
#
#     def __add__(self, other):
#         return Cell(self.quantity + other.quantity)
#
#     def __sub__(self, other):
#         return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')
#
#     def __mul__(self, other):
#         return Cell(int(self.quantity * other.quantity))
#
#     def __truediv__(self, other):
#         return Cell(round(self.quantity // other.quantity))
#
#     def make_order(self, cells_in_row):
#         row = ''
#         for i in range(int(self.quantity / cells_in_row)):
#             row += f'{"*" * cells_in_row} \\n'
#         row += f'{"*" * (self.quantity % cells_in_row)}'
#         return row
#
#
# cells1 = Cell(33)
# cells2 = Cell(9)
# print(cells1)
# print(cells1 + cells2)
# print(cells2 - cells1)
# print(cells2.make_order(5))
# print(cells1.make_order(10))
# print(cells1 / cells2)

class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self._count + other._count)

    def __sub__(self, other: "Cell") -> "Cell":
        if self._count > other._count:
            return Cell(self._count - other._count)

        # raise ValueError(f"{self._count} - {other._count}: impossible operation")
        print(f"{self._count} - {other._count}: impossible operation")

    def __mul__(self, other: "Cell") -> "Cell":
        return Cell(self._count * other._count)

    def __truediv__(self, other: "Cell") -> "Cell":
        return Cell(self._count // other._count)

    def make_order(self, per_row: int) -> str:
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"


if __name__ == '__main__':
    c1 = Cell(14)
    print(c1)
    c2 = Cell(1)
    print(c2)

    print(c1 + c2)
    print(c1 - c2)
    print(c2 - c1)
    print(c2 - c2)
    print(c1 * c2)
    print(c1 / c2)
    print((c1 * c2).make_order(23))
