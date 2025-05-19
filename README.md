# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Perusahaan Edutech ini mengalami tingkat attrition (keluar masuk karyawan) yang cukup tinggi, melebihi angka wajar (>10%). Kondisi ini menyebabkan ketidakstabilan dalam tim, meningkatnya biaya rekrutmen dan pelatihan, serta berkurangnya produktivitas secara keseluruhan.

### Permasalahan Bisnis
1. Tingginya angka attrition (>16%) pada karyawan.
2. Tidak adanya indikator atau sistem pemantauan risiko attrition secara real-time.
3. Belum diketahui secara pasti faktor-faktor utama penyebab karyawan keluar dari perusahaan.

### Cakupan Proyek
1. Menganalisis data HR untuk mengetahui karakteristik karyawan yang keluar.
2. Mengidentifikasi fitur/variabel penting yang memengaruhi attrition menggunakan machine learning.
3. Membuat dashboard interaktif di Metabase untuk membantu pengambilan keputusan.

### Persiapan

Sumber data: ....


#### 1. Install Library yang Dibutuhkan
```bash
pip install -r requirements.txt
```

#### 2. Setup Metabase
Menggunakan Metabase untuk pembuatan dashboard:
```bash
docker pull metabase/metabase:v0.46.4
docker run -p 3000:3000 --name metabase metabase/metabase
```
Akses Metabase melalui [http://localhost:3000/setup](http://localhost:3000/setup).

#### 3. Setup Database Supabase
- Buat akun di [Supabase](https://supabase.com/dashboard/sign-in).
- Buat project baru dan salin URI database.
- Kirim dataset ke database menggunakan SQLAlchemy:

```python
from sqlalchemy import create_engine
URL = "DATABASE_URL"  # Ganti dengan URL database Supabase
engine = create_engine(URL)
df.to_sql('dataset', engine)
```

## Business Dashboard
Dashboard dibangun menggunakan Metabase, dengan data yang terhubung melalui Supabase PostgreSQL. Dashboard ini menyajikan:

* Ringkasan total karyawan, attrition rate, dan overtime.
* Visualisasi faktor penyebab attrition (OverTime, JobLevel, dll).
* Distribusi attrition berdasarkan Department dan JobRole.
* Tabel karyawan berisiko tinggi berdasarkan hasil model prediksi.  

Akses Dashboard: 
## Conclusion
Hasil analisis menunjukkan bahwa attrition di perusahaan didorong oleh faktor-faktor seperti OverTime, rendahnya Job Satisfaction, dan tingkat pendapatan. Model Random Forest digunakan untuk memprediksi risiko attrition dan memberikan feature importance.

Dashboard interaktif di Metabase kini dapat digunakan oleh tim HR untuk memantau kondisi tenaga kerja dan melakukan intervensi lebih awal terhadap karyawan yang berisiko.

### Rekomendasi Action Items (Optional)
* Mengurangi beban lembur terutama pada divisi dengan attrition tinggi.
* Meningkatkan engagement dan kepuasan kerja di level jabatan rendah.
* Menggunakan dashboard Metabase secara berkala untuk memantau risiko keluar karyawan.
