# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 1, 2, 5
# Вывод: 1, 3, 5, 7, 9

def progr( a1, d, n ):
    arrProgr = list()
    
    i = 1
    while i <= n:
        an = a1 + (i-1) * d
        arrProgr.append( an )
        i += 1
    
    return arrProgr
	

a1 = int( input('Введите первый элемент ' ))
d = int( input('Введите разность ' ))
n = int( input('Введите количество элементов ' ))

myProgr = progr( a1, d, n )
print( *myProgr )