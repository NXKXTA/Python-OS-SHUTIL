import os
import shutil


def find_files(dir_path, extension):
    if not os.path.isdir(dir_path):
        print("Директория не найдена.")
        return []

    if not extension.startswith('.'):
        print("Неверное расширение.")
        return []

    files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(extension):
                files.append(os.path.join(root, file))

    return files


def main():
    # Запрашиваем у пользователя путь к директории
    dir_path = input("Введите путь к директории: ")

    # Запрашиваем у пользователя расширение файлов
    extension = input("Введите расширение файлов: ")

    # Ищем файлы
    files = find_files(dir_path, extension)

    # Выводим список найденных файлов
    if files:
        print("Найденные файлы:")
        for file in files:
            print(file)
    else:
        print("Файлов с заданным расширением не найдено.")
