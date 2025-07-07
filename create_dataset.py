import os # untuk bekerja dengan sistem file (membaca direktori dan file)
import pickle # untuk menyimpan dan memuat objek (data dan label) ke dalam file
import mediapipe as mp # untuk mendeteksi tangan (hand tracking)
import cv2 # untuk pemrosesan gambar dan video
import matplotlib.pyplot as plt # digunakan untuk visualisasi


mp_hands = mp.solutions.hands # mengakses solusi deteksi tangan dari mediapipe
mp_drawing = mp.solutions.drawing_utils # menggambar landmark tangan
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3) # inisialisasi objek deteksi tangan dari mediapipe

DATA_DIR = './data'

data = []
labels = []

for dir_ in os.listdir(DATA_DIR): # membaca daftar semua folder yang ada di direktori 'data'
    dir_path = os.path.join(DATA_DIR, dir_)
    if os.path.isdir(dir_path):  # pastikan hanya direktori yang diproses
        for img_path in os.listdir(dir_path):
            data_aux = []
            x_ = []
            y_ = []

            img = cv2.imread(os.path.join(dir_path, img_path)) # membaca gambar dari file
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # mengubah gambar dari format BGR (default OpenCV) ke format RGB 

            results = hands.process(img_rgb) # memproses gambar untuk mendeteksi tangan dan landmark di dalam gambar
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        
                        # menyimpan koordinat x dan y dari semua landmark tangan
                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        # menyimpan fitur landmark yang sudah dinormalisasi
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))

                data.append(data_aux) # menambahkan fitur dari gambar ke dalam list 'data'
                labels.append(dir_) # menyimpan label (nama kelas dari folder) yang sesuai dengan data

# simpan data dan label ke file pickle
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)