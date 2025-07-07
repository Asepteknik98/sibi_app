import os
import cv2
import numpy as np

# Fungsi augmentasi sederhana
def augment(img):
    imgs = [img]
    # Flip horizontal
    imgs.append(cv2.flip(img, 1))
    # Rotasi
    for angle in [-15, 15]:
        (h, w) = img.shape
        M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
        imgs.append(cv2.warpAffine(img, M, (w, h), borderMode=cv2.BORDER_REFLECT))
    # Brightness
    imgs.append(cv2.convertScaleAbs(img, alpha=1.2, beta=30))
    imgs.append(cv2.convertScaleAbs(img, alpha=0.8, beta=-30))
    # Blur
    imgs.append(cv2.GaussianBlur(img, (5,5), 0))
    return imgs

img_size = 64

total_aug = 0
for i in range(26):
    folder = f"data/{i}"
    if os.path.exists(folder):
        imgs = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg','.jpeg','.png'))]
        for fname in imgs:
            fpath = os.path.join(folder, fname)
            img = cv2.imread(fpath, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img = cv2.resize(img, (img_size, img_size))
            aug_imgs = augment(img)
            for idx, aug in enumerate(aug_imgs[1:]):  # skip original
                aug_name = f"aug_{os.path.splitext(fname)[0]}_{idx}.jpg"
                aug_path = os.path.join(folder, aug_name)
                cv2.imwrite(aug_path, aug)
                total_aug += 1
        print(f"{folder}: {len(imgs)} gambar asli, {total_aug} gambar augmentasi ditambah.")
print("Selesai augmentasi dataset!") 