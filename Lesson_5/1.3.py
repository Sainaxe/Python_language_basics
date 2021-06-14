'''
task3
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('task3.txt', 'r', encoding='utf-8') as file_3:
    salary = []
    less_than_20k_salary = []
    list_3 = file_3.read().split('\n')
    for i in list_3:
        i = i.split()
        if int(i[1]) < 20000:
           less_than_20k_salary.append(i[0])
        salary.append(i[1])
print(f'Salary less than 20,000: {less_than_20k_salary}, average salary {sum(map(int, salary)) / len(salary)} rub.')
