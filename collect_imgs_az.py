import cv2
import os

print("Script pengambilan gambar gesture A-Z dari webcam.")
print("- Masukkan huruf (A-Z) yang ingin direkam.")
print("- Tekan SPASI untuk menyimpan gambar.")
print("- Tekan ESC untuk ganti huruf atau keluar.")

img_size = 64

def get_label_idx(char):
    return ord(char.upper()) - 65

while True:
    huruf = input("Masukkan huruf (A-Z, atau ketik 'exit' untuk keluar): ").strip().upper()
    if huruf == 'EXIT':
        break
    if len(huruf) != 1 or not ('A' <= huruf <= 'Z'):
        print("Input tidak valid. Masukkan satu huruf A-Z.")
        continue
    label_idx = get_label_idx(huruf)
    folder = f"data/{label_idx}"
    os.makedirs(folder, exist_ok=True)
    cap = cv2.VideoCapture(0)
    count = len([f for f in os.listdir(folder) if f.lower().endswith(('.jpg','.jpeg','.png'))])
    print(f"Ambil gambar untuk huruf '{huruf}' (folder: {folder}). Tekan SPASI untuk simpan, ESC untuk selesai.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_resized = cv2.resize(frame, (320, 240))
        cv2.putText(frame_resized, f'Huruf: {huruf} | Gambar: {count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
        cv2.imshow('Ambil Gambar Gesture', frame_resized)
        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break
        elif key == 32:  # SPASI
            img_name = f"{count}.jpg"
            img_path = os.path.join(folder, img_name)
            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img_save = cv2.resize(img_gray, (img_size, img_size))
            cv2.imwrite(img_path, img_save)
            print(f"Disimpan: {img_path}")
            count += 1
    cap.release()
    cv2.destroyAllWindows()
print("Selesai ambil gambar gesture!") 