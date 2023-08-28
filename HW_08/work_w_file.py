# Программа должна выводить данные
import os

INFILE = "data.txt"
OUTFILE = "new_data.txt"
ENC = "utf-8"


def check(text):
    if len(text.split()) == 4:
        if text.split()[3].isdigit():
            return True
        else:
            print("Номер введен неправильно!")
            print("Нужно ввести номер телефона без знака +")
            return False
    else:
        print("Нужно ввести (Фамилию Имя Отчество Номер)!")
        return False

def check_number(tel_number):
    with open(INFILE, "r", encoding=ENC) as f:
        for line in f:
            if tel_number in line:
                return True
        return False

def write(text):
    if check(text):
        with open(INFILE, "a", encoding=ENC) as f:
            f.writelines(text)
            f.writelines("\n")
            print("Успешно")
    else:
        return -1


def read_all():
    with open(INFILE, "r", encoding=ENC) as f:
        for line in f:
            print(line[:-1])


def get_by_name(name):
    with open(INFILE, "r", encoding=ENC) as f:
        for line in f:
            if name in line:
                print(line)


def alter_line(words, alter):
    words = str(words)
    info = words.split()
    if len(info) != 2:
        print("Вы ввели некорректные данные!")
        return -1
    rewrite = False
    with open(INFILE, encoding=ENC) as infile, open(OUTFILE, 'w', encoding=ENC) as outfile:
        for line in infile:
            if not rewrite and str(info[0]) in str(line) and str(info[1]) in str(line):
                if alter:
                    new_line = str(input("На кого хотите заменить? "))
                    if check(new_line):
                        outfile.writelines(new_line + "\n")
                        print("Строка успешно заменена")
                    else:
                        return -1
                else:
                    print("Строка успешно удалена")
                rewrite = True
            elif len(line) > 2: # проверка на пустую линию
                outfile.writelines(line)

    if rewrite:
        os.remove(INFILE)
        os.rename(OUTFILE, INFILE)
    else:
        os.remove(OUTFILE)
        print(f"Строка с пользователем {info[0]} {info[1]} не найдена")
