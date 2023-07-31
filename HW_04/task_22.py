# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = 0
while n <= 0:
    n = int( input('Введите число n ' ))
    
m = 0
while m <= 0:
    m = int( input('Введите число m ' ))

listN = list()
listM = list()

print('Введите числа первого набора')
i = 0
while i < n:
    listN.append( int( input() ) )
    i += 1

print('Введите числа второго набора')
i = 0
while i < m:
    listM.append( int( input() ) )
    i += 1

listN = list( set( listN ) )
listM = list( set( listM ) )
result = list()

for item in listN:
    if listM.count( item ):
        result.append( item )

result.sort()
print( result )