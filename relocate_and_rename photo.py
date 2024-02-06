import os
import shutil

# Шлях до початкової та цільової папок
source_folder = "E:\SignDetection\dataMarko"# "повний/шлях/до/початкової/папки/
destination_folder ="./data"# "повний/шлях/до/цільової/папки"
selected_folders = [f'{i}' for i in range(33)]
second_loop_lst = [f"{i}.jpg" for i in range(100)]

for dir_ in selected_folders:

    for img in second_loop_lst:
        full_path = os.path.join(source_folder, dir_, img)
        print(full_path)

        filename_without_extension, extension = os.path.splitext(img)
        number = int(filename_without_extension)
        new_filename = f"{number+300}{extension}"
        print(new_filename)
        shutil.move(full_path, os.path.join(destination_folder,dir_, new_filename))
        print(f"Файл {img} був переміщений та перейменований на {new_filename}")