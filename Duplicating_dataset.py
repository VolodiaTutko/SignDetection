import os

import cv2
import time
import random
import numpy as np

imgSize = 300

DATA_DIR = './data'
selected_folders = ['./0', './1', './2', './3', './4', './5', './6', './7', './8', './9', './10', './11', './12', './13', './14', './15', './16', './17', './18', './19', './20', './21', './22', './23', './24', './25', './26', './27', './28', './29', './30', './31', './32']#'./0','./1', './2', './3', './4'
start_time = time.time()
for dir_ in os.listdir(DATA_DIR):
    counter = 0
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        print(f'{dir_, img_path}')
        image = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        for i in range(11):
            rotate_angle = random.uniform(-10, 10)  # обертання випадковим кутом
            imgRotated = cv2.warpAffine(image,cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2),
                                                                      rotate_angle,1.0),
                                        (image.shape[1], image.shape[0]))
            flip_flag = np.random.choice((0,1))  # випадково відзеркалити або ні
            imgRotated = cv2.flip(imgRotated, flip_flag)

            # Збереження нового зображення
            target_dir = os.path.join(DATA_DIR, dir_)
            os.makedirs(target_dir, exist_ok=True)

            cv2.imwrite(f'{DATA_DIR}/{dir_}/{100+counter}.jpg', imgRotated)
            counter += 1


end_time = time.time()
execution_time = end_time - start_time

print(f"Час виконання: {execution_time} секунд")