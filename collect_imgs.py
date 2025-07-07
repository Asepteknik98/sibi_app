import os
import cv2

DATA_DIR = './data' # lokasi tempat menyimpan dataset
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR) # membuat folder bernama 'data' jika folder tersebut belum ada.

number_of_classes = 3 # jumlah kelas data yang akan dikumpulkan
dataset_size = 100 # jumlah gambar yang dikumpulkan untuk setiap kelas

cap = cv2.VideoCapture(0) # mengakses webcam komputer (kamera default)
for j in range(number_of_classes): # melakukan iterasi sebanyak jumlah kelas
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA) # menampilkan video dari webcam dan menambahkan teks
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'): # menunggu pengguna untuk menekan tombol 'Q'
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read() # mengumpulkan gambar dari webcam dan menyimpannya ke dalam direktori sesuai dengan kelasnya
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame) # gambar disimpan dengan format .jpg dan diberi nama berurutan

        counter += 1

cap.release() # akses ke webcam ditutup
cv2.destroyAllWindows() # jendela OpenCV ditutup
