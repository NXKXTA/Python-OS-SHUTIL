import os

putdopapki = input("Введите путь до директории: ")
if not os.path.exists(putdopapki):
    print("Введены некорректные данные")
    exit()

tip = '.' + input("Введите расширение: ")
esttakie = 0
for put, papki, faily in os.walk(putdopapki):
    for file in faily:
        file = os.path.join(put, file)
        if os.path.splitext(file)[-1] == tip:
            print(file)
            esttakie = 1

if not esttakie:
    print("Файлов с таким расширением нет")
