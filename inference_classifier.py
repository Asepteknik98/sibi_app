import pickle
import cv2
import mediapipe as mp
import numpy as np
import os
import string
import pyttsx3
import time

# Mapping label ke huruf A-Z
def label_to_char(label):
    return chr(65 + label)  # 0->A, 1->B, ..., 25->Z

# Inisialisasi TTS
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Load model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']
img_size = model_dict.get('img_size', 64)

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

last_pred = None
last_tts_time = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    h, w, c = frame.shape
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    pred_char = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Crop ROI tangan
            x_list = [lm.x for lm in hand_landmarks.landmark]
            y_list = [lm.y for lm in hand_landmarks.landmark]
            xmin, xmax = int(min(x_list) * w), int(max(x_list) * w)
            ymin, ymax = int(min(y_list) * h), int(max(y_list) * h)
            # Tambahkan margin
            margin = 30
            xmin = max(0, xmin - margin)
            ymin = max(0, ymin - margin)
            xmax = min(w, xmax + margin)
            ymax = min(h, ymax + margin)
            roi = frame[ymin:ymax, xmin:xmax]
            if roi.size == 0:
                continue
            roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            roi_resized = cv2.resize(roi_gray, (img_size, img_size))
            roi_flat = roi_resized.flatten().reshape(1, -1)
            # Prediksi
            pred_label = model.predict(roi_flat)[0]
            pred_char = label_to_char(pred_label)
            # Tampilkan hasil prediksi di frame
            cv2.putText(frame, f'Prediksi: {pred_char}', (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.imshow('ROI', roi_resized)
    # TTS: jika gesture A-Z terdeteksi dan berbeda dari sebelumnya, ucapkan huruf tersebut
    if pred_char is not None and pred_char != last_pred and time.time() - last_tts_time > 1.5:
        engine.say(pred_char)
        engine.runAndWait()
        last_tts_time = time.time()
    last_pred = pred_char
    cv2.imshow('Teman SIBI - Inference A-Z', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
