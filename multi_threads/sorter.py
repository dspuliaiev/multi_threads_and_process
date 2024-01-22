import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def sort_files(source_folder, output_folder):
    source_path = Path(source_folder)
    output_path = Path(output_folder)

    # Створюємо папку виведення, якщо вона не існує
    output_path.mkdir(parents=True, exist_ok=True)

    def move_file(file_path):
        try:
            # Отримуємо розширення файлу
            file_extension = file_path.suffix.lower()

            # Створюємо папку у вихідному каталозі за розширенням
            output_folder_ext = output_path / file_extension
            output_folder_ext.mkdir(parents=True, exist_ok=True)

            # Переносимо файл у відповідну папку
            shutil.move(file_path, output_folder_ext / file_path.name)
        except Exception as e:
            print(f"Error moving file {file_path}: {e}")

    def process_folder(folder):
        # Отримуємо список файлів у папці
        files = [file for file in folder.iterdir() if file.is_file()]

        # Переносимо файли у відповідні папки паралельно за допомогою пулу потоків
        with ThreadPoolExecutor() as executor:
            executor.map(move_file, files)

        # Рекурсивно обробляємо всі підкаталоги у папці
        for subfolder in folder.iterdir():
            if subfolder.is_dir():
                process_folder(subfolder)

    # Запускаємо обробку папки "Хлам"
    process_folder(source_path)

if __name__ == "__main__":
    # Параметри командного рядка
    source_folder = input("Введіть шлях до папки 'Хлам': ")
    output_folder = input("Введіть шлях до вихідної папки: ")

    # Запускаємо сортування файлів
    sort_files(source_folder, output_folder)

    print("Сортування завершено.")