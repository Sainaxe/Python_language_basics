'''
task3
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 >= arg2 and arg3 >= arg2:
        return arg1 + arg3
    else:
        return arg2 + arg3

print\
    (f'Result - {my_func(int(input("Enter 1st argument: ")),int(input("enter 2nd argument: ")),int(input("enter 3rd argument: ")))}')
