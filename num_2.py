import os, shutil

ves = 0
putdopapki = input("Введите путь до заархивированной директории: ")
if not os.path.exists(putdopapki):
    print("Введены некорректные данные")
    exit()
newPapka = "novayaPapka"
try:
    shutil.unpack_archive(putdopapki, newPapka)
except shutil.ReadError:
    print("Введены некорректные данные")
    exit()

for put, papki, faily in os.walk(newPapka):
    for file in faily:
        file = os.path.join(put, file)
        ves += os.path.getsize(file)
print("Размер файлов:", ves, "байт")

shutil.rmtree(newPapka)
