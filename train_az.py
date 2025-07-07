import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import pickle

# Mapping label ke huruf
label_to_char = {i: chr(65 + i) for i in range(26)}
char_to_label = {v: k for k, v in label_to_char.items()}

data_dir = 'data'
img_size = 64  # Ukuran gambar yang akan di-resize

def load_dataset():
    X, y = [], []
    for label in range(26):
        folder = os.path.join(data_dir, str(label))
        if not os.path.exists(folder):
            continue
        for fname in os.listdir(folder):
            if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
                fpath = os.path.join(folder, fname)
                img = cv2.imread(fpath, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    continue
                img = cv2.resize(img, (img_size, img_size))
                X.append(img.flatten())
                y.append(label)
    X = np.array(X)
    y = np.array(y)
    return X, y

def visualize_samples():
    fig, axes = plt.subplots(2, 13, figsize=(18, 3))
    for label in range(26):
        folder = os.path.join(data_dir, str(label))
        imgs = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        ax = axes[label // 13, label % 13]
        if imgs:
            img = cv2.imread(os.path.join(folder, imgs[0]), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (img_size, img_size))
            ax.imshow(img, cmap='gray')
        ax.set_title(label_to_char[label])
        ax.axis('off')
    plt.suptitle('Contoh Gambar Setiap Kelas (A-Z)')
    plt.tight_layout()
    plt.show()

def main():
    print('Membaca dataset...')
    X, y = load_dataset()
    print(f'Total gambar: {len(X)}')
    if len(X) == 0:
        print('Dataset kosong!')
        return
    print('Visualisasi contoh gambar...')
    visualize_samples()

    print('Split data training/test...')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    print('Training SVM...')
    clf = SVC(kernel='linear', probability=True)
    clf.fit(X_train, y_train)

    print('Evaluasi...')
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f'Akurasi: {acc*100:.2f}%')

    print('Confusion Matrix:')
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[label_to_char[i] for i in range(26)])
    disp.plot(xticks_rotation=45)
    plt.show()

    print('Simpan model ke model.p')
    with open('model.p', 'wb') as f:
        pickle.dump({'model': clf, 'img_size': img_size}, f)
    print('Selesai!')

    cv2.imshow('ROI', roi_resized)

if __name__ == '__main__':
    main() 