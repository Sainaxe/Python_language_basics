'''
task7
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json

per = dict()
average_profit = 0
num = 0
with open("task7.txt", encoding="utf-8") as task_7:
    for line in task_7:
        name_of_the_organization, type_of_ownership, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit >= 0:
            average_profit += profit
            num += 1
        per[name_of_the_organization] = profit
    print(f"Summary profit: {average_profit}")
average_profit /= num
print(f"Average profit (only for profitable companies): {average_profit}")
with open("task7.json", "w", encoding="utf-8") as task_7:
    json.dump([per, {"average_profit": average_profit}], task_7, ensure_ascii=False)
