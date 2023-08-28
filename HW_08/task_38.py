# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести фамилию, и Вы должны реализовать функционал для изменения и удаления данных
import os

INFILE = "data.txt"
OUTFILE = "new_data.txt"
ENC = "utf-8"


def change_data( whatChange, changeOn ):
    with open(INFILE, 'r', encoding=ENC) as f:
        oldData = f.read()
        
    newData = oldData.replace( whatChange , changeOn )
    
    with open(INFILE, 'w', encoding=ENC) as f:
        f.write(newData)
            

def del_data( whatDel ):
    newData = ''
    with open(INFILE, 'r', encoding=ENC) as f:
        for line in f:
        	if line.find( whatDel ) == -1:
                 newData += line
    
    with open(INFILE, 'w', encoding=ENC) as f:
        f.write(newData)