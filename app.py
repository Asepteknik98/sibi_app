from flask import Flask, render_template, request, redirect, url_for, session, flash
import subprocess
import os
import signal

app = Flask(__name__)
app.secret_key = 'teman_sibi_secret_key'  # Ganti dengan secret key yang aman di produksi

# Hardcoded credentials
def check_login(email, password):
    return email == 'admin@email.com' and password == 'admin123'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if check_login(email, password):
            session['user_email'] = email
            return redirect(url_for('main'))
        else:
            flash('Email atau password salah!', 'danger')
    return render_template('login.html')

@app.route('/main')
def main():
    user_email = session.get('user_email')
    if not user_email:
        return redirect(url_for('login'))
    username = "Sherly Octavia Anggraeni"  # Hardcode username
    return render_template('main.html', username=username)

@app.route('/deteksi', methods=['GET', 'POST'])
def deteksi():
    if request.method == 'POST':
        # Tombol Start ditekan, jalankan inference_classifier.py
        subprocess.Popen(['python', 'inference_classifier.py'])
        flash('Deteksi isyarat telah dimulai.', 'success')
        return redirect(url_for('main'))
    # GET: hanya tampilkan tombol Start
    return render_template('deteksi.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Placeholder untuk daftar
@app.route('/register')
def register():
    flash('Fitur daftar belum tersedia.', 'info')
    return redirect(url_for('login'))

@app.route('/perpus')
def perpus():
    return render_template('perpus.html')

@app.route('/informasi')
def informasi():
    return render_template('informasi.html')

if __name__ == '__main__':
    app.run(debug=True) 