# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Perusahaan Edutech ini mengalami tingkat attrition (keluar masuk karyawan) yang cukup tinggi, melebihi angka wajar (>10%). Kondisi ini menyebabkan ketidakstabilan dalam tim, meningkatnya biaya rekrutmen dan pelatihan, serta berkurangnya produktivitas secara keseluruhan.

### Permasalahan Bisnis
1. Tingginya angka attrition (>10%) pada karyawan.
2. Tidak adanya indikator atau sistem pemantauan risiko attrition secara real-time.
3. Belum diketahui secara pasti faktor-faktor utama penyebab karyawan keluar dari perusahaan.

### Cakupan Proyek
1. Menganalisis data HR untuk mengetahui karakteristik karyawan yang keluar.
2. Mengidentifikasi fitur/variabel penting yang memengaruhi attrition menggunakan machine learning.
3. Membuat dashboard interaktif di Metabase untuk membantu pengambilan keputusan.

### Persiapan
#### Sumber Dataset
Dataset mencakup berbagai atribut seperti:  
* usia
* jenis pekerjaan
* tingkat kepuasan kerja
* tingkat pendapatan
* status lembur    
Data kemudian diproses melalui tahapan pembersihan, encoding, dan pembagian data untuk training dan evaluasi model.  
**Sumber data:** [Database](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

### Setup Environment
Langkah-langkah persiapan environment adalah sebagai berikut:
#### 1. Buat Environment Python
```bash
conda create --name bpds_sub1 python=3.9.15 -y
conda activate bpds_sub1
```

#### 2. Install Library yang Dibutuhkan
```bash
pip install -r requirements.txt
```

#### 3. Setup Metabase
Menggunakan Metabase untuk pembuatan dashboard:
```bash
docker pull metabase/metabase:v0.46.4
docker run -d -p 3000:3000 --name metabase metabase/metabase
```
Akses Metabase melalui [http://localhost:3000/setup](http://localhost:3000/setup).

#### 4. Setup Database Supabase
- Buat akun di [Supabase](https://supabase.com/dashboard/sign-in).
- Buat project baru dan salin URI database.
- Kirim dataset ke database menggunakan SQLAlchemy:

```python
from sqlalchemy import create_engine
URL = "DATABASE_URL"  # Ganti dengan URL database Supabase
engine = create_engine(URL)
df.to_sql('dataset', engine)
```

## Modeling
Model yang digunakan untuk memprediksi risiko attrition adalah Random Forest Classifier, karena kemampuannya menangani fitur kategorikal dan numerik secara bersamaan serta memberikan interpretasi lewat feature importance.
### Evaluasi Model
* Akurasi: 0.87
* Precision dan Recall seimbang
* Confusion matrix menunjukkan model mampu mendeteksi karyawan yang berisiko keluar dengan cukup baik.
    ![Image](https://github.com/user-attachments/assets/2c48243d-6cdf-4713-b658-e8f545793425)
  
### Faktor Penting Penyebab Attrition
Berdasarkan feature importance dari Random Forest, faktor-faktor dominan penyebab attrition antara lain:  
* OverTime (lembur)
* JobSatisfaction
* MonthlyIncome
* JobLevel
* YearsAtCompany
  
## Business Dashboard
Dashboard dibangun menggunakan Metabase, dengan data yang terhubung melalui Supabase PostgreSQL. Dashboard ini menyajikan:
![Image](https://github.com/user-attachments/assets/777bcf59-6dff-4f84-bfc0-65152847d74b)
* Ringkasan total karyawan, attrition rate, dan overtime.
* Visualisasi faktor penyebab attrition (OverTime, JobLevel, dll).
* Distribusi attrition berdasarkan Department dan JobRole.
* Tabel karyawan berisiko tinggi berdasarkan hasil model prediksi.  

**Akses Dashboard melalui akun metabase:**  
Username : rosalia03rrrbkl@gmail.com  
Password : metabaserosa01 

## Menjalankan Sistem Machine Learning
### Menjalankan Sistem Machine Learning Secara Lokal
1. Pastikan Anda sudah memiliki file berikut di direktori kerja:
   - `app.py` (kode aplikasi Streamlit)
   - `model.pkl` atau `model.joblib` (model machine learning yang sudah dilatih)
   - `scaler.pkl` (scaler yang digunakan untuk preprocessing fitur)
   - `features.txt` (daftar nama fitur yang digunakan model)
2. Jalankan aplikasi Streamlit:
```bash
streamlit run app.py
```
### Menjalankan Prototype Machine Learning yang sudah dideploy
Jika prototype sudah di-deploy di Streamlit Community, dapat mengaksesnya melalui link berikut:
- [Link Prototype Streamlit](https://sub1bpds-ofmzv7wgsysss7fbxvywec.streamlit.app/)

### Cara Menggunakan Aplikasi
* Jika ingin mencoba prediksi dengan data lokal, siapkan file CSV dengan format fitur yang sesuai (misal: `data_prediction.csv`, ada dalam file project).  
* Upload data dengan mengunggah file CSV secara langsung untuk melakukan prediksi. Hasil prediksi akan ditampilkan dalam tabel, termasuk nilai probabilitas risiko dropout.

## Conclusion
Proyek ini berhasil mengidentifikasi faktor-faktor utama penyebab attrition dan membangun sistem pendukung keputusan berbasis data. Model prediksi yang dibangun menggunakan **Random Forest** memberikan hasil akurat dan dapat diandalkan untuk memantau risiko keluar karyawan.

Dashboard yang dibangun memungkinkan tim HR untuk:
* Melihat overview kondisi attrition secara real-time
* Mengidentifikasi karyawan berisiko tinggi
* Mengambil tindakan intervensi lebih awa

### Rekomendasi Action Items (Optional)
* **Mengurangi beban lembur** terutama pada divisi dengan attrition tinggi.
* Meningkatkan **engagement dan kepuasan kerja** di level jabatan rendah.
* Menggunakan dashboard Metabase secara berkala untuk memantau risiko keluar karyawan.
