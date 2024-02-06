import os

import cv2
import time
import random
import numpy as np

imgSize = 300

DATA_DIR = './data'
start_time = time.time()
selected_folders = [f'{i}' for i in range(33)]
second_loop_lst = [f"{i}.jpg" for i in range(400)]

for dir_ in selected_folders:
    counter = 0
    print(f'{dir_}')
    for img_path in second_loop_lst:

        image = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        for i in range(11):
            rotate_angle = random.uniform(-10, 10)  # обертання випадковим кутом
            imgRotated = cv2.warpAffine(image,cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2),
                                                                      rotate_angle,1.0),
                                        (image.shape[1], image.shape[0]))
            flip_flag = np.random.choice((0,1))  # випадково відзеркалити або ні
            if flip_flag == 1:
                imgRotated = cv2.flip(imgRotated, flip_flag)

            # Збереження нового зображення
            target_dir = os.path.join(DATA_DIR, dir_)
            os.makedirs(target_dir, exist_ok=True)

            cv2.imwrite(f'{DATA_DIR}/{dir_}/{400+counter}.jpg', imgRotated)
            counter += 1


end_time = time.time()
execution_time = end_time - start_time

print(f"Час виконання: {execution_time} секунд")