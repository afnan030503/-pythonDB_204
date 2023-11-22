import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fungsi untuk menentukan prediksi berdasarkan nilai tertinggi
def predict_major(mat, phy, chem, bio, indo, eng, hist, geo, econ, socio):
    subjects = [mat, phy, chem, bio, indo, eng, hist, geo, econ, socio]
    max_subject_index = subjects.index(max(subjects))
    
def predict_major(mat, phy, chem, bio, indo, eng, hist, geo, econ, socio):
    if mat > max(phy, chem, bio, indo, eng, hist, geo, econ, socio):
        return "Pendidikan Matematika"
    elif phy > max(mat, chem, bio, indo, eng, hist, geo, econ, socio):
        return "ASTRONOT"
    elif chem > max(mat, phy, bio, indo, eng, hist, geo, econ, socio):
        return "Bom Atom"
    elif bio > max(mat, phy, chem, indo, eng, hist, geo, econ, socio):
        return "Kedokteran"
    elif indo > max(mat, phy, chem, bio, eng, hist, geo, econ, socio):
        return "Bahasa"
    elif eng > max(mat, phy, chem, bio, indo, hist, geo, econ, socio):
        return "Bahasa Asing"
    elif hist > max(mat, phy, chem, bio, indo, eng, geo, econ, socio):
        return "Pendongeng"
    elif geo > max(mat, phy, chem, bio, indo, eng, hist, econ, socio):
        return "Pendidikan Geografi"
    elif econ > max(mat, phy, chem, bio, indo, eng, hist, geo, socio):
        return "FEB"
    elif socio > max(mat, phy, chem, bio, indo, eng, hist, geo, econ):
        return "Teknik"
    else:
        return "Belum dapat diprediksi"

# Fungsi untuk menambahkan nilai ke dalam database SQLite
def add_data_to_db(name, mat, phy, chem, bio, indo, eng, hist, geo, econ, socio, prediction):
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            matematika INTEGER,
            fisika INTEGER,
            kimia INTEGER,
            biologi INTEGER,
            bahasa_indonesia INTEGER,
            bahasa_inggris INTEGER,
            sejarah_indonesia INTEGER,
            geografi INTEGER,
            ekonomi INTEGER,
            sosiologi INTEGER,
            prediksi_fakultas TEXT
        )
    ''')

    # Menambahkan data ke dalam tabel
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, matematika, fisika, kimia, biologi, bahasa_indonesia, 
        bahasa_inggris, sejarah_indonesia, geografi, ekonomi, sosiologi, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, mat, phy, chem, bio, indo, eng, hist, geo, econ, socio, prediction))

    conn.commit()
    conn.close()

# Fungsi yang dijalankan ketika tombol submit ditekan
def submit_button_pressed():
    name = entry_nama.get()
    mat = int(entry_mat.get())
    phy = int(entry_phy.get())
    chem = int(entry_chem.get())
    bio = int(entry_bio.get())
    indo = int(entry_indo.get())
    eng = int(entry_eng.get())
    hist = int(entry_hist.get())
    geo = int(entry_geo.get())
    econ = int(entry_econ.get())
    socio = int(entry_socio.get())

    prediction = predict_major(mat, phy, chem, bio, indo, eng, hist, geo, econ, socio)
    
    # Menampilkan hasil prediksi
    messagebox.showinfo("Prediksi Fakultas", f"Prediksi fakultas untuk {name}: {prediction}")

    # Menambahkan data ke dalam database
    add_data_to_db(name, mat, phy, chem, bio, indo, eng, hist, geo, econ, socio, prediction)

# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Prediksi Fakultas")

# Membuat label dan entry untuk nama siswa
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Membuat label dan entry untuk nilai Matematika
label_mat = tk.Label(root, text="Nilai Matematika:")
label_mat.pack()
entry_mat = tk.Entry(root)
entry_mat.pack()

# Membuat label dan entry untuk nilai Fisika
label_phy = tk.Label(root, text="Nilai Fisika:")
label_phy.pack()
entry_phy = tk.Entry(root)
entry_phy.pack()

# Membuat label dan entry untuk nilai Kimia
label_chem = tk.Label(root, text="Nilai Kimia:")
label_chem.pack()
entry_chem = tk.Entry(root)
entry_chem.pack()

# Membuat label dan entry untuk nilai Biologi
label_bio = tk.Label(root, text="Nilai Biologi:")
label_bio.pack()
entry_bio = tk.Entry(root)
entry_bio.pack()

# Membuat label dan entry untuk nilai Bahasa Indonesia
label_indo = tk.Label(root, text="Nilai Bahasa Indonesia:")
label_indo.pack()
entry_indo = tk.Entry(root)
entry_indo.pack()

# Membuat label dan entry untuk nilai Bahasa Inggris
label_eng = tk.Label(root, text="Nilai Bahasa Inggris:")
label_eng.pack()
entry_eng = tk.Entry(root)
entry_eng.pack()

# Membuat label dan entry untuk nilai Sejarah Indonesia
label_hist = tk.Label(root, text="Nilai Sejarah Indonesia:")
label_hist.pack()
entry_hist = tk.Entry(root)
entry_hist.pack()

# Membuat label dan entry untuk nilai Geografi
label_geo = tk.Label(root, text="Nilai Geografi:")
label_geo.pack()
entry_geo = tk.Entry(root)
entry_geo.pack()

# Membuat label dan entry untuk nilai Ekonomi
label_econ = tk.Label(root, text="Nilai Ekonomi:")
label_econ.pack()
entry_econ = tk.Entry(root)
entry_econ.pack()

# Membuat label dan entry untuk nilai Sosiologi
label_socio = tk.Label(root, text="Nilai Sosiologi:")
label_socio.pack()
entry_socio = tk.Entry(root)
entry_socio.pack()

# Membuat tombol submit
button_submit = tk.Button(root, text="Submit", command=submit_button_pressed)
button_submit.pack()

root.mainloop()
