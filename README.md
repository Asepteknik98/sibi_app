# Bahasa Isyarat python

Sign language detector with Python, OpenCV and Mediapipe !

[![Watch the video](https://img.youtube.com/vi/MJCSjXepaAM/0.jpg)](https://www.youtube.com/watch?v=MJCSjXepaAM)
# SIBI App - Sistem Deteksi Bahasa Isyarat Indonesia (SIBI)

Selamat datang di repositori **SIBI App**!  
Proyek ini bertujuan untuk membangun aplikasi deteksi bahasa isyarat Indonesia (SIBI) berbasis **Computer Vision** dan **Machine Learning**, yang dapat membantu dalam komunikasi antara penyandang tunarungu dengan masyarakat umum.

---

## 🔍 Fitur Utama

- Deteksi gerakan tangan untuk mengenali bahasa isyarat Indonesia
- Real-time video processing
- Tampilan antarmuka sederhana dan responsif
- Model klasifikasi gesture menggunakan dataset kustom
- Dukungan integrasi kamera langsung

---

## 📦 Teknologi yang Digunakan

- Python
- OpenCV
- TensorFlow / Keras (jika digunakan)
- MediaPipe (jika digunakan)
- Streamlit (jika berbasis web)
- dll.

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Clone Repositori

```bash
git clone https://github.com/Asepteknik98/sibi_app.git
cd sibi_app
python -m venv venv
source venv/bin/activate       # Untuk Linux/macOS
venv\Scripts\activate          # Untuk Windows

pip install -r requirements.txt

streamlit run app.py

python app.py

sibi_app/
│
├── dataset/            # Folder untuk dataset gesture bahasa isyarat
├── model/              # Model deteksi yang sudah dilatih
├── app.py              # Entry point aplikasi (Streamlit atau GUI lainnya)
├── utils.py            # Fungsi bantu seperti preprocessing atau prediksi
├── README.md
└── requirements.txt    # Daftar dependensi

🤝 Kontribusi
Kami terbuka untuk kontribusi dari siapa pun yang tertarik dengan pengembangan aplikasi ini!
Silakan fork repositori ini, buat branch baru, dan kirimkan pull request.

📣 Lisensi
Project ini bersifat open-source dan dilisensikan di bawah MIT License.

📬 Kontak
Jika ada pertanyaan, saran, atau kolaborasi, silakan hubungi:

Asep Teknik
📧 Email: [Email Anda di sini]
🔗 GitHub: https://github.com/Asepteknik98

⭐️ Jangan lupa untuk memberikan bintang (⭐) pada repo ini jika Anda merasa project ini bermanfaat!
yaml
Copy
Edit


---

### Tips Supaya README Anda Terlihat Profesional:

1. **Gunakan Bahasa yang Formal dan Informatif.**
2. **Gunakan Format Markdown dengan baik** (heading, list, kode blok).
3. **Cantumkan struktur folder** agar developer lain bisa memahami struktur proyek.
4. **Sediakan instruksi yang jelas** untuk instalasi dan penggunaan.
5. **Sertakan lisensi dan kontak** agar bisa digunakan secara legal dan transparan.

Jika Anda menggunakan gambar/video deteksi gesture, sangat disarankan untuk menambahkan GIF atau screenshot hasil aplikasi di README agar lebih menarik.

---

Saya bisa bantu juga buat file `requirements.txt` atau menambahkan badge GitHub jika dibutuhkan. Ingin saya bantu buatkan juga?
