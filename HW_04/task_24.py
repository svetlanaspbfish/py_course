# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = 0
while n <= 0:
    n = int( input('Введите число N ' ))

i = 0
harvestOnPlants = list()
while i < n:
    curHarvest = -1
    while curHarvest < 0:
        curHarvest = int( input(f'Введите число ягод на кусте { i + 1 } '))
    harvestOnPlants.append( curHarvest )
    i += 1
    
print( harvestOnPlants )

maxHarvest = 0
i = 0
while i < n:
    ileft =  i + 1 if ( i + 1 ) < n else 0
    iright = i - 1 if ( i - 1 ) >= 0 else n - 1
    curHarvest = harvestOnPlants[ i ] + harvestOnPlants[ ileft ] + harvestOnPlants[ iright ]
    if ( curHarvest > maxHarvest ):
        maxHarvest = curHarvest
    i += 1

print( maxHarvest )