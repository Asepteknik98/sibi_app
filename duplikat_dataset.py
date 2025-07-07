import os
import shutil

TARGET = 100  # jumlah minimal gambar per folder

for i in range(26):
    folder = f"data/{i}"
    if os.path.exists(folder):
        imgs = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg','.jpeg','.png'))]
        n = len(imgs)
        if n == 0:
            print(f"Folder {folder} kosong, lewati.")
            continue
        # Duplikasi hingga mencapai TARGET
        idx = 0
        while len(imgs) < TARGET:
            src = os.path.join(folder, imgs[idx % n])
            dst = os.path.join(folder, f"dup_{len(imgs)}_{imgs[idx % n]}")
            shutil.copy(src, dst)
            imgs.append(f"dup_{len(imgs)}_{imgs[idx % n]}")
            idx += 1
        print(f"{folder}: {len(imgs)} gambar")
print("Selesai! Setiap folder sekarang minimal punya 100 gambar.") 