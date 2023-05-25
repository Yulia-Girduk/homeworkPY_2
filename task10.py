# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


# 1 - орел, 0 - решка.
from random import randint


print('Количество монеток n:')
n = int(input())
if n > 0:
    countCoin1 = 0
    countCoin0 = 0

    for i in range(1,n+1):
        coin = randint(0,1)
        print(f'{i} монета имеет сторону {coin}')
        if coin == 1:
            countCoin1 += 1
        if coin == 0:
            countCoin0 += 1
    if countCoin1 < countCoin0:
        minCoin = countCoin1
    elif countCoin0 < countCoin1:
        minCoin = countCoin0
    else:
        minCoin = countCoin0
    print(f'Минимальное количество монет, которое нужно перевернуть = {minCoin}')        
else:
    print('Ввели число меньше 0!!!')
