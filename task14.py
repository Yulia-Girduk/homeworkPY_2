# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

num = int(input("Введите число: "))
power = 1
i = 0
if num > 0:
    while power <= num:
        print(power, end =', ')
        power = power*2    
else:
    print('Не верно ввели данные число меньше либо равно 0!!!')