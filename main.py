import os, sys # Импорт модулей в одной строке - плохая практика

def exampleFunction( arg1,arg2 ): # Пробелы вокруг аргументов и неправильный стиль именования
    unused_var = 42 # Неиспользуемая переменная

    if arg1 > arg2: print("Arg1 is greater!") # Однострочный if без отступов
    else:
        print ('Arg2 is greater or equal!') # Лишний пробел после print

    for i in range(0, 10): # range(0, 10) можно заменить на range(10)
     print("Number:",i) # Отсутствует отступ

    with open("test.txt", "w") as f:
        f.write("Hello") # Нет проверки закрытия файла

# Вызов функции
exampleFunction(1,2)
