import pickle

import cv2
import mediapipe as mp
import numpy as np

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3, max_num_hands=1)

labels_dict = {0: 'А', 1: 'Б', 2: 'В', 3: 'Г', 4: 'Ґ', 5: 'Д', 6: 'Е', 7: 'Є', 8: 'Ж', 9: 'З', 10: 'И', 11: 'І', 12: 'Ї', 13: 'Й', 14: 'К', 15: 'Л', 16: 'М', 17: 'Н', 18: 'О', 19: 'П', 20: 'Р', 21: 'С', 22: 'Т', 23: 'У', 24: 'Ф', 25: 'Х', 26: 'Ц', 27: 'Ч', 28: 'Ш', 29: 'Щ', 30: 'Ю', 31: 'Я', 32: 'Ь'}
result = [];
while True:

    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()

    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10

        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10

        prediction = model.predict([np.asarray(data_aux)])
        print(prediction)
        predicted_character = labels_dict[int(prediction[0])]
        print(predicted_character)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1.3, (0, 0, 0), 3,
                    cv2.LINE_AA)
        result.append(predicted_character)
        print(''.join(result))
    cv2.imshow('frame', frame)
    cv2.waitKey(1500)


cap.release()
cv2.destroyAllWindows()