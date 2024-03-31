import os
import shutil

src = input("Введите путь до директории src: ")
dst = input("Введите путь до директории dst: ")

if not (os.path.exists(src) and os.path.exists(dst)):
    print("Введены некорректные данные")
    exit()

kartinki = ['.png', '.jpg', '.jpeg', '.WebP']

for put, papki, files in os.walk(src):
    for file in files:
        file = os.path.join(put, file)
        if os.path.splitext(file)[-1] in kartinki:
            shutil.copy(file, dst)
shutil.make_archive(dst, "zip")
