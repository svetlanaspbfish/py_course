# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

def findIndexesBetweenMinAndMax( arr, min, max ):
    arrIndexes = list()
    i = 0
    while i < len( arr ):
        if arr[ i ] <= max and arr[ i ] >= min :
            arrIndexes.append( i )
        i += 1
    return arrIndexes

min = int( input('Введите минимум ' ))
max = int( input('Введите максимум ' ))

print('Введите элементы списка через пробел: ')
arr = [ int(x) for x in input().split() ]
indexes = findIndexesBetweenMinAndMax( arr, min, max )

print('Искомые индексы: ')
print( *indexes )