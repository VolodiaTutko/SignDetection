# import os
# import pickle
# import time
# import mediapipe as mp
# import cv2
# import numpy as np
#
#
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
#
# hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3,max_num_hands=1)
#
#
# DATA_DIR = './data'
# selected_folders = ['./0', './1', './2', './3', './4', './5', './6', './7', './8', './9', './10', './11', './12', './13', './14', './15', './16', './17', './18', './19', './20', './21', './22', './23', './24', './25', './26', './27', './28', './29', './30', './31', './32']#'./0','./1', './2', './3', './4'
#
# data = []
# labels = []
# counter = 0
# start_time = time.time()
# for dir_ in selected_folders:
#     for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
#         data_aux = []
#
#         x_ = []
#         y_ = []
#
#         img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
#         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#         results = hands.process(img_rgb)
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 for i in range(len(hand_landmarks.landmark)):
#                     x = hand_landmarks.landmark[i].x
#                     y = hand_landmarks.landmark[i].y
#
#                     x_.append(x)
#                     y_.append(y)
#
#                 for i in range(len(hand_landmarks.landmark)):
#                     x = hand_landmarks.landmark[i].x
#                     y = hand_landmarks.landmark[i].y
#                     data_aux.append(x - min(x_))
#                     data_aux.append(y - min(y_))
#
#             data.append(data_aux)
#             labels.append(counter)
#     counter += 1
# end_time = time.time()
# execution_time = end_time - start_time
#
# print(f"Час виконання: {execution_time} секунд")
# f = open('data.pickle', 'wb')
# pickle.dump({'data': data, 'labels': labels}, f)
# f.close()
#
import pickle
import time
import mediapipe as mp
import cv2
import numpy as np
import json

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3, max_num_hands=1)

DATA_DIR = './data'
selected_folders = [f'{i}' for i in range(33)]

data, labels = [], np.array([])
counter = 0
second_loop_lst = [f"{i}.jpg" for i in range(4800)]

start_time = time.time()
for dir_ in selected_folders:
    print(dir_)

    for img_path in second_loop_lst:
        data_aux = []

        x_, y_ = [], []

        img = cv2.imread("./data/" + dir_ + "/" + img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                range_ = range(len(hand_landmarks.landmark))

                x_ = [hand_landmarks.landmark[i].x for i in range_]
                y_ = [hand_landmarks.landmark[i].y for i in range_]

                for i in range_:
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels = np.append(labels, counter)
    counter += 1

end_time = time.time()
execution_time = end_time - start_time

print(f"Exec time: {execution_time} sec")
print(f"Exec time: {round(execution_time / 60, 4)} minutes")

f = open('data4800.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()

# obj = json.dumps({'data': data, 'labels': labels.tolist()})
#
# with open('data4.json', 'w') as f:
#     f.write(obj)
