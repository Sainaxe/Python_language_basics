'''
task5
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint as rd

with open("task5.txt", "w+", encoding="utf8") as task_5:
    task_5.write(" ".join([str(rd(0, 99)) for _ in range(99)]))
    task_5.seek(0)
    print(f"SUMM: {(sum(map(int, task_5.readline().split())))}")
