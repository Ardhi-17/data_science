# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, tingginya jumlah siswa yang tidak menyelesaikan pendidikannya (dropout) menjadi masalah besar. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang berpotensi dropout agar dapat diberikan bimbingan khusus.

### Tujuan Proyek
- Melakukan analisis eksploratif terhadap data siswa untuk memahami pola-pola yang berkaitan dengan perilaku dropout.
- Mengembangkan model prediksi  berbasis machine learning untuk memprediksi kemungkinan siswa akan dropout.
- Membangun aplikasi prediksi berbasis Streamlit agar hasil analisis dan model prediktif dapat digunakan oleh pihak manajemen secara praktis dan efisien.

## Permasalahan Bisnis
**1. Tingginya Tingkat Dropout:**

Jumlah siswa yang tidak menyelesaikan pendidikan di Jaya Jaya Institut cukup signifikan, yang berdampak pada reputasi institusi dan efisiensi operasional.

**2. Keterlambatan Identifikasi Risiko Dropout:**

Tidak adanya sistem yang dapat mendeteksi dini siswa yang berpotensi dropout, sehingga bimbingan atau intervensi sering kali terlambat dilakukan.

**3. Kurangnya Wawasan Berbasis Data:**

Institusi belum memanfaatkan data siswa secara maksimal untuk menganalisis faktor-faktor yang menyebabkan dropout.

**4. Keterbatasan Akses Teknologi oleh Pengguna Non-Teknis**

Pihak pengelola dan pengajar membutuhkan alat bantu yang intuitif untuk mengakses hasil prediksi dan mengambil keputusan dengan cepat tanpa harus memahami teknis machine learning.

## Cakupan Proyek
### **Eksplorasi Data (EDA)**
    - Visualisasi distribusi fitur numerik (histogram, boxplot).
    - Visualisasi fitur kategorikal (bar chart, pie chart).
    - Multivariate analysis, bivariate analysis dan univariate analysis untuk memahami hubungan antar fitur.
### **Preprocessing Data**
    - Imputasi nilai hilang, jika ada.  
    - Mengatasi Nilai duplikat
    - Encoding kategorikal (One-Hot atau Label Encoding).  
    - Feature Engineering (jika diperlukan).
    - Scaling numerik (StandardScaler).  
    - Pembagian data: 80% train, 20% test.
### **Modeling**
    - Pelatihan model dengan algoritma Random Forest.
### **Evaluation**
    - Mengukur performa model menggunakan metrik yang relevan (accuracy, precision, recall, F1-score, ROC-AUC).
    - Cross-validation untuk meminimalkan bias.
    - Mengidentifikasi fitur yang paling signifikan.
### **Deployment Aplikasi**
    - Notebook berisi seluruh pipeline (EDA, preprocessing, modeling).  
    - **Streamlit App**: Model berupa web yang memungkinkan prediksi real-time.
    - **Metabase** : Dashboard yang menampilkan faktor penting dalam memonitor performa siswa.
### **Rekomendasi:** 
    - Memberikan rekomendasi tindakan berdasarkan hasil analisis dan prediksi model untuk mengurangi tingkat dropout.

## Persiapan
**Sumber Data**
Dataset diambil dari [Students Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv).


Contoh 5 Baris Pertama:
| Marital\_status | Application\_mode | Application\_order | Course | … |   GDP | Status   |
| --------------: | ----------------: | -----------------: | -----: | - | ----: | -------- |
|               1 |                17 |                  5 |    171 | … |  1.74 | Dropout  |
|               1 |                15 |                  1 |   9254 | … |  0.79 | Graduate |
|               1 |                 1 |                  5 |   9070 | … |  1.74 | Dropout  |
|               1 |                17 |                  2 |   9773 | … | -3.12 | Graduate |
|               2 |                39 |                  1 |   8014 | … |  0.79 | Graduate |

**Rangkuman Dataset**

    - Jumlah baris: 4.424
    - Jumlah kolom: 37

**Jenis Data**

    - Terdapat 29 kolom dengan tipe data integer (int64)
    - 7 kolom bertipe desimal (float64)
    - 1 kolom dengan tipe objek (object)  yaitu kolom Status.

**Kondisi Data**

    - Seluruh kolom telah terisi lengkap, tanpa missing value (null).
    - Kolom Status bertipe object dan diduga berfungsi sebagai target/label klasifikasi (misal: Graduate, Dropout, dsb)

Proyek ini memerlukan lingkungan Python 3.8+ untuk menjalankan analisis data dan model machine learning, serta Docker untuk menjalankan dashboard Metabase.

Setup environment:
untuk menjalankan kode notebook, pastikan Anda telah menginstal library yang diperlukan dengan menggunakan 

```
pip install -r requirements.txt
```

lalu jalankan kode notebook dengan menggunakan google colab atau local environment.

**Menjalankan Analisis :**
1. Pastikan semua dependensi telah terinstal dengan benar.
2. Jalankan file notebook.ipynb menggunakan Jupyter Notebook atau Google Colab.
3. Notebook mencakup:
   - Exploratory Data Analysis (EDA) didalamnya terdapat: univariate anlysis, mutlivariate analysis dan bivariate analysis.
   - Preprocessing dan pembersihan data
   - Training model random forest
   - Evaluasi performa model
   - Menyimpan model ke dalam file .pkl dan .joblib

**Berikut insight dari visualisasi hasil model machine learning.**

![Image](https://github.com/user-attachments/assets/f6c45106-bce2-404b-ad69-9bc18c73dbc8)

![Image](https://github.com/user-attachments/assets/fcdffdd8-e5a4-40b2-b064-71283d153aca)

**Confusion Matrix**

- Benar memprediksi 189 siswa “tidak dropout” (True Negative)
- Benar memprediksi 546 siswa “dropout” (True Positive)
- Masih ada 80 siswa “tidak dropout” yang diprediksi dropout (False Positive)
- Masih ada 41 siswa “dropout” yang diprediksi tidak dropout (False Negative)
  
**Feature Importance**

Faktor akademik paling berpengaruh terhadap prediksi dropout:

- Jumlah mata kuliah lulus dan nilai semester 1 & 2 (terutama semester 2) adalah fitur terpenting untuk model.
- Fitur “Curricular_units_2nd_sem_approved” (unit lulus semester 2) dan “Curricular_units_2nd_sem_grade” (nilai semester 2) menempati urutan teratas, artinya prestasi akademik semester 2 sangat krusial dalam menentukan risiko dropout.
- Usia saat masuk kuliah, jurusan (Course), dan kelancaran pembayaran UKT juga termasuk fitur penting, namun dampaknya masih di bawah faktor akademik.
- Fitur dengan pengaruh kecil: mode aplikasi, status debitur, status beasiswa, dan kualifikasi pendidikan sebelumnya—semuanya punya dampak, tapi tidak sebesar prestasi akademik.


**Menjalankan Dashboard Metabase :**

**Dashboard dapat dijalankan melalui tautan yang ada pada bagian Business Dashboard**

Gunakan kredensial login berikut untuk akses awal:
- Email: root@mail.com
- Password: root123

## Business Dashboard

Dashboard ini dibuat untuk menganalisis data mahasiswa dan memantau faktor-faktor utama yang mempengaruhi status kelulusan (seperti Dropout, enrolled dan Graduate) pada institusi pendidikan Jaya Jaya.Visualisasi pada dashboard ini dikembangkan menggunakan Metabase yang terhubung ke database PostgreSQL Supabase, serta dijalankan melalui Docker untuk memudahkan deployment dan pengelolaan.

1. **Pastikan Docker sudah terinstall** di komputer Anda.
2. **Jalankan perintah berikut** di terminal untuk memulai prototype:
   ```
   docker compose up -d
   ```
3. Tunggu hingga semua container berjalan dengan baik.

4. **Akses dashboard** melalui link berikut:
   
**http://localhost:3000/public/dashboard/57519df1-23ec-4d76-bcdd-62e9b33fd291**

(Jalankan Metabase via docker untuk melihat dashboard)
Gunakan kredensial login berikut untuk akses awal:

- Email: root@mail.com
- Password: root123

**Tujuan Dashboard**

- Memberikan gambaran cepat mengenai status mahasiswa di institusi, seperti jumlah yang lulus, dropout, dan masih terdaftar.
- Mengidentifikasi tren dan pola yang mempengaruhi status dropout siswa berdasarkan berbagai karakteristik (misal: nilai, gender, latar belakang, dsb).
- Membantu pihak manajemen atau akademik dalam mengambil keputusan berbasis data untuk meningkatkan tingkat kelulusan dan menurunkan angka dropout.

**Visualisasi yang Ditampilkan**

**Metrik Utama Mahasiswa:**
- Total Mahasiswa: 4.424
- Distribusi Gender:

    - Female (Perempuan): 64,8%
    - Male (Laki-laki): 35,2%

- Status Mahasiswa:

    - Graduate (Lulus): 2.209
    - Dropout (Keluar): 1.421
    - Enrolled (Masih Aktif): 794

**Faktor-faktor yang Dianalisis pada Dashboard:**
Faktor-faktor yang Dianalisis pada Dashboard:
- Status Mahasiswa berdasarkan Gender:

    - Jumlah dropout antara perempuan dan laki-laki hampir seimbang (Female: 720, Male: 701).
    - Tidak ada perbedaan signifikan risiko dropout berdasarkan gender.

- Status Mahasiswa berdasarkan Program Studi:
        
    - Program studi Nursing memiliki jumlah mahasiswa dan kasus dropout tertinggi.
    - Program lain dengan dropout tinggi: Social Service, Management.
    - Beberapa jurusan dengan mahasiswa sedikit juga tetap mengalami dropout.
    
- Status Mahasiswa berdasarkan Rentang Usia:

    - Dropout paling banyak terjadi di kelompok usia 15–22,5 tahun (693 orang), disusul kelompok 22,5–30 tahun (343 orang).
    - Mahasiswa muda lebih rawan dropout dibanding kelompok usia lebih tua.

- Status Mahasiswa berdasarkan Nilai Akademik:

    - Mahasiswa dropout memiliki nilai rata-rata semester 1 dan 2 paling rendah (Semester 1: 7,26 | Semester 2: 5,9).
    - Mahasiswa yang lulus (graduate) punya nilai rata-rata tertinggi (Semester 1: 12,64 | Semester 2: 12,7).
    - Terdapat gap nilai akademik yang signifikan antara mahasiswa dropout, enrolled, dan graduate.

    Status Mahasiswa berdasarkan Beasiswa:

    - Mahasiswa tanpa beasiswa jauh lebih banyak yang dropout (1.287) dibanding yang menerima beasiswa (134).
    - Penerima beasiswa memiliki peluang bertahan dan lulus lebih besar.

Visualisasi pada dashboard menampilkan tren, distribusi, dan insight terkait faktor-faktor utama yang mempengaruhi status Dropout mahasiswa di institusi pendidikan Jaya Jaya.

![Image](https://github.com/user-attachments/assets/0f4bddab-f49d-43e6-874d-3b5ca376155d)

![Image](https://github.com/user-attachments/assets/2beb3bc4-c358-4ada-8db0-c55c133b2e98)

![Image](https://github.com/user-attachments/assets/26b45cee-b027-4b80-b9ce-376b4ce922b2)

![Image](https://github.com/user-attachments/assets/c26db746-3c72-45e0-8e30-dfc01d201229)

![Image](https://github.com/user-attachments/assets/6d8b5dcb-b139-46be-a9ec-d4e68bd5b6f2)

![Image](https://github.com/user-attachments/assets/e4d698ea-430b-4c88-bfe1-bdf26c798e5f)

![Image](https://github.com/user-attachments/assets/9d8cf1b8-47ee-4b92-afa6-a511f35ac38b)


**Insight Utama**

- Mahasiswa dengan nilai rata-rata rendah pada semester 1 & 2 paling rentan dropout.
- Jurusan dengan mahasiswa terbanyak (Nursing, Social Service, Management) menyumbang dropout tertinggi — bisa jadi karena volume, tapi perlu perhatian khusus pada beban studi dan sistem dukungan.
- Mahasiswa muda (15–22,5 tahun) mendominasi angka dropout – indikasi masalah adaptasi dan transisi dari SMA ke perguruan tinggi.
- Beasiswa berperan besar sebagai proteksi risiko dropout — penerima beasiswa jarang keluar di tengah jalan.
- Tidak ada perbedaan signifikan risiko dropout berdasarkan gender (laki-laki dan perempuan hampir sama).
- Penurunan rata-rata nilai di semester 2 juga perlu diwaspadai, bisa jadi indikator awal masalah akademik.
- Performa jurusan sangat bervariasi — beberapa jurusan dengan mahasiswa sedikit malah punya rata-rata nilai sangat rendah dan tetap ada dropout.
- Fokus utama pencegahan dropout: mahasiswa baru, nilai rendah, jurusan dengan angka dropout tinggi, dan kelompok tanpa beasiswa.

## Menjalankan Sistem Machine Learning
### Cara Menjalankan Prototype Sistem Machine Learning (Streamlit)

1. **Pastikan Python sudah terinstall** di komputer Anda (disarankan versi 3.8 ke atas).
2. **Pastikan file berikut tersedia di direktori proyek Anda:**
   - `model_prediksi.joblib`
   - `scaler.joblib`
   - `model_prediksi.pkl`
   - `prediction.py`
   - `dashboard.py`
   - `requirements.txt`
   
   File-file ini wajib ada agar aplikasi Streamlit dapat berjalan dengan baik di lokal.

3. **Install Streamlit dan dependensi lain** yang diperlukan dengan menjalankan perintah berikut di terminal:
   ```
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit** dengan perintah:
   ```
   streamlit run dashboard.py
   ```
   (Pastikan Anda berada di direktori proyek yang berisi file `dashboard.py`)

5. **Akses prototype sistem machine learning (Streamlit)** melalui link berikut di browser Anda:
   
   [App Prediksi Dropout via Streamlit](https://laskaraiawaw.streamlit.app/)

7. Setelah halaman Streamlit terbuka, Anda dapat menguji fitur prediksi status mahasiswa dengan memasukkan data yang diperlukan pada form yang tersedia di aplikasi Streamlit.

**Catatan:**  
- Untuk menghentikan aplikasi, tekan `Ctrl+C` di terminal tempat Streamlit dijalankan.

![Image](https://github.com/user-attachments/assets/0ad54f0a-b0a6-4493-ab6e-3b6061c609bc)

![Image](https://github.com/user-attachments/assets/28cc54df-85f8-4000-ab58-d8efb1c5997f)

## Conclusion
Proyek ini telah berhasil mengembangkan sistem prediksi untuk mendeteksi mahasiswa yang berpotensi dropout di Institut Jaya Jaya. Model machine learning yang digunakan menunjukkan akurasi yang baik (sekitar 85% berdasarkan hasil evaluasi), serta mampu mengidentifikasi faktor-faktor utama penyebab dropout, seperti nilai akademik yang rendah dan tingkat kehadiran yang kurang. Dashboard interaktif yang dikembangkan memudahkan staf institusi dalam memantau risiko dropout secara visual, sementara prototipe sistem dapat diintegrasikan ke dalam operasional institusi untuk mendukung intervensi dini. Dengan demikian, proyek ini memberikan solusi berbasis data yang dapat meningkatkan retensi mahasiswa dan efektivitas proses bimbingan.

**Model machine learning mengidentifikasi mahasiswa berisiko tinggi dropout berdasarkan fitur-fitur utama berikut:**

- Nilai rata-rata semester 1 & 2
- Jumlah mata kuliah lulus pada semester 1 & 2
- Status pembayaran UKT, status penerima beasiswa, dan status debitur
- Usia saat mendaftar, mode pendaftaran, serta kualifikasi pendidikan sebelumnya

**Insight utama:**

- Mahasiswa dengan nilai akademik rendah, pembayaran UKT yang tidak lancar, tidak menerima beasiswa, dan mengambil beban studi sedikit memiliki risiko dropout yang lebih tinggi.
- Terdapat beberapa jurusan/program studi, mode pendaftaran, dan kelompok usia tertentu yang menunjukkan tingkat dropout lebih tinggi dibandingkan kelompok lainnya.


## Rekomendasi Action Items
Berikut adalah rekomendasi tindakan yang disarankan untuk Institut Jaya Jaya:

1. **Implementasi Sistem Prediktif & Early Warning**
   - Integrasikan prototipe machine learning ke dalam sistem manajemen mahasiswa untuk memantau risiko dropout secara real-time.
   - Terapkan sistem early warning yang secara otomatis mengirimkan notifikasi kepada dosen wali atau pihak akademik jika ada mahasiswa yang terdeteksi berisiko tinggi.

2. **Program Intervensi & Bimbingan Khusus**
   - Prioritaskan pendampingan akademik, konseling, serta dukungan finansial bagi mahasiswa yang teridentifikasi berisiko tinggi.
   - Sediakan program bimbingan khusus dan monitoring perkembangan mahasiswa secara berkala.

3. **Pelatihan Staf Akademik**
   - Lakukan pelatihan rutin kepada staf akademik mengenai penggunaan dashboard, interpretasi hasil prediksi, dan langkah intervensi yang tepat berdasarkan data.

4. **Optimalisasi & Peningkatan Pengumpulan Data**
   - Perluas cakupan data yang dikumpulkan, misalnya dengan menambahkan data riwayat absensi, data keluarga, serta tingkat keterlibatan mahasiswa dalam kegiatan kampus untuk meningkatkan akurasi model prediksi.

5. **Monitoring dan Evaluasi Berkala**
   - Gunakan dashboard secara rutin dalam rapat evaluasi untuk mendukung pengambilan keputusan berbasis data.
   - Lakukan evaluasi performa model setiap semester agar model tetap relevan dan akurat mengikuti perubahan pola mahasiswa.

Dengan menerapkan langkah-langkah di atas, diharapkan sistem prediksi dropout dapat berjalan optimal dan memberikan dampak nyata dalam meningkatkan retensi mahasiswa di Institut Jaya Jaya.
