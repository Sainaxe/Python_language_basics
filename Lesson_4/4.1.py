'''
task1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''


def pay():
    try:
        time = float(input('Worked in hours: '))
        salary = int(input('Hourly rate: '))
        bonus = int(input('Premium: '))
        total = time * salary + bonus
        print(f'Total salary:  {total}')
    except ValueError:
        return print('Not a number')


pay()
