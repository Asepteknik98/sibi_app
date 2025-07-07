import os
import zipfile
import shutil
import glob
import sys

# Pastikan kaggle sudah terinstall
try:
    import kaggle
except ImportError:
    print('Menginstall kaggle...')
    os.system('pip install kaggle')

# Download dataset dari Kaggle
DATASET = 'grassknoted/asl-alphabet'
ZIP_NAME = 'asl-alphabet.zip'
EXTRACT_DIR = 'asl_alphabet_train'

print('Download dataset dari Kaggle...')
os.system(f'kaggle datasets download -d {DATASET} -f {ZIP_NAME} --unzip')

# Ekstrak zip jika belum diekstrak
if not os.path.exists(EXTRACT_DIR):
    with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
        zip_ref.extractall('.')

# Mapping folder A-Z ke data/0 ... data/25
print('Mapping folder A-Z ke data/0 ... data/25 ...')
if not os.path.exists('data'):
    os.makedirs('data')

for idx, huruf in enumerate([chr(65+i) for i in range(26)]):
    src = os.path.join(EXTRACT_DIR, huruf)
    dst = os.path.join('data', str(idx))
    if os.path.exists(dst):
        shutil.rmtree(dst)
    if os.path.exists(src):
        shutil.copytree(src, dst)
        print(f'{huruf} -> data/{idx} ({len(os.listdir(dst))} gambar)')
    else:
        print(f'Folder {src} tidak ditemukan!')

print('Selesai! Dataset siap digunakan di folder data/0 ... data/25') 