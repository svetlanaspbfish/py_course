# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да    
#     Вывод: Парам пам-пам  

ruVowel = 'аоуыэяеёюи'

def vovelsCount( str ):
    str = list( filter( lambda x: x in  ruVowel, str ) )
    return len( str )
    

phrases = input('Введите стихотворение. Фразы отделяются пробелами, слова дефисами: ').split()

vovelsInPhrases = list( map( vovelsCount, phrases ) )
differentVowelCounts = set( vovelsInPhrases )

if ( len( differentVowelCounts ) > 1 ):
    print('Пам парам')
else:
    print('Парам пам-пам')