import streamlit as st
import pandas as pd
from data_preprocessing import data_preprocessing
from prediction import predict_status

# ===============================
# KONFIGURASI TEMA & STYLING
# ===============================
st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS untuk styling
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stNumberInput, .stSelectbox, .stRadio {
        background-color: white;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stForm {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #34495e;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ===============================
# HEADER & DESKRIPSI UTAMA
# ===============================
st.markdown("""
# 🎓 Aplikasi Prediksi Dropout Mahasiswa  
**Selamat datang di aplikasi prediksi status mahasiswa!**  
Aplikasi ini membantu memprediksi **status kelulusan mahasiswa**—apakah *Dropout* atau *Tetap Kuliah (Stay)*—berdasarkan data akademik dan pribadi mahasiswa.  
Silakan isi formulir berikut dengan data mahasiswa untuk mendapatkan prediksi akurat:
""")

st.divider()

# ===============================
# FORMULIR INPUT
# ===============================
with st.form("prediksi_mahasiswa", clear_on_submit=False):
    st.markdown("### 📋 Data Akademik & Pribadi Mahasiswa")
    
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("📚 Data Akademik")
        age = st.number_input('Umur saat mendaftar', min_value=17, max_value=70, value=20, help="Masukkan umur mahasiswa saat pertama kali mendaftar kuliah", key="age")
        curricular_units_1st_sem_approved = st.number_input('Jumlah Mata Kuliah Lulus Semester 1', min_value=0, max_value=26, value=5, key="cu1_approved")
        curricular_units_1st_sem_grade = st.number_input('Nilai Rata-rata Semester 1', min_value=0.0, max_value=20.0, value=12.0, step=0.1, format="%.2f", key="cu1_grade")
        curricular_units_2nd_sem_approved = st.number_input('Jumlah Mata Kuliah Lulus Semester 2', min_value=0, max_value=20, value=5, key="cu2_approved")
        curricular_units_2nd_sem_grade = st.number_input('Nilai Rata-rata Semester 2', min_value=0.0, max_value=20.0, value=12.0, step=0.1, format="%.2f", key="cu2_grade")
    
    with col2:
        st.subheader("💼 Data Keuangan & Akademik")
        debtor = st.radio('Apakah memiliki tanggungan pembayaran (Debitur)?', options=[1, 0], format_func=lambda x: "Ya" if x==1 else "Tidak", key="debtor")
        scholarship_holder = st.radio('Apakah penerima beasiswa?', options=[1, 0], format_func=lambda x: "Ya" if x==1 else "Tidak", key="scholarship")
        tuition_fees_up_to_date = st.radio('Status pembayaran UKT?', options=[1, 0], format_func=lambda x: "Lancar" if x==1 else "Tidak Lancar", key="tuition")
    
        course_dict = {
            33: "Biofuel Production Technologies",
            171: "Animation and Multimedia Design",
            8014: "Social Service (evening attendance)",
            9003: "Agronomy",
            9070: "Communication Design",
            9085: "Veterinary Nursing",
            9119: "Informatics Engineering",
            9130: "Equinculture",
            9147: "Management",
            9238: "Social Service",
            9254: "Tourism",
            9500: "Nursing",
            9556: "Oral Hygiene",
            9670: "Advertising and Marketing Management",
            9773: "Journalism and Communication",
            9853: "Basic Education",
            9991: "Management (evening attendance)"
        }
        course_label = st.selectbox(
            'Pilih Program Studi (Jurusan)',
            options=[f"{kode} - {nama}" for kode, nama in course_dict.items()],
            index=list(course_dict.keys()).index(171),
            key="course"
        )
        course = int(course_label.split(" - ")[0])
        
        application_mode_dict = {
            1: "1st phase - Jalur Umum",
            2: "Ordinance No. 612/93",
            5: "1st phase - Jalur Khusus (Azores Island)",
            7: "Pemilik gelar pendidikan lain",
            10: "Ordinance No. 854-B/99",
            15: "Mahasiswa Internasional (Sarjana)",
            16: "1st phase - Jalur Khusus (Madeira Island)",
            17: "2nd phase - Jalur Umum",
            18: "3rd phase - Jalur Umum",
            26: "Ordinance No. 533-A/99, item b2) (Plan Lain)",
            27: "Ordinance No. 533-A/99, item b3 (Kampus Lain)",
            39: "Jalur Umum >23 tahun",
            42: "Transfer",
            43: "Ganti Jurusan",
            44: "Lulusan Spesialisasi Teknologi",
            51: "Ganti kampus/jurusan",
            53: "Lulusan Diploma Short Cycle",
            57: "Ganti kampus/jurusan (Internasional)"
        }
        application_mode_label = st.selectbox(
            'Jalur Pendaftaran',
            options=[f"{kode} - {nama}" for kode, nama in application_mode_dict.items()],
            index=0,
            key="app_mode"
        )
        application_mode = int(application_mode_label.split(" - ")[0])
        
        previous_qualification_dict = {
            1: "Pendidikan Menengah (SMA/Sederajat)",
            2: "S1/Sarjana",
            3: "Gelar Lain",
            4: "Magister (S2)",
            5: "Doktor (S3)",
            6: "Frekuensi Pendidikan Tinggi",
            9: "Kelas 12 belum lulus",
            10: "Kelas 11 belum lulus",
            12: "Lainnya - Kelas 11",
            14: "Kelas 10",
            15: "Kelas 10 belum lulus",
            19: "Pendidikan Dasar Siklus 3 (9-11 tahun)",
            38: "Pendidikan Dasar Siklus 2 (6-8 tahun)",
            39: "Kursus Spesialisasi Teknologi",
            40: "Gelar Pendidikan Tinggi (Siklus 1)",
            42: "Kursus Teknis Tinggi Profesional",
            43: "Magister Pendidikan Tinggi (Siklus 2)"
        }
        previous_qualification_label = st.selectbox(
            'Kualifikasi Pendidikan Sebelumnya',
            options=[f"{kode} - {nama}" for kode, nama in previous_qualification_dict.items()],
            index=0,
            key="prev_qual"
        )
        previous_qualification = int(previous_qualification_label.split(" - ")[0])

    st.markdown("")

    submitted = st.form_submit_button("🔮 Prediksi Status Mahasiswa", use_container_width=True)

    # ===============================
    # PREDIKSI & OUTPUT
    # ===============================
    if submitted:
        # Kumpulkan input user jadi DataFrame
        data = pd.DataFrame({
            'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
            'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
            'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
            'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
            'Age_at_enrollment': [age],
            'Debtor': [debtor],
            'Scholarship_holder': [scholarship_holder],
            'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
            'Course': [course],
            'Application_mode': [application_mode],
            'Previous_qualification': [previous_qualification]
        })
        with st.spinner("🔄 Memproses prediksi..."):
            hasil = predict_status(data)
        # Misalkan hasil prediksi: 1 = Dropout, 0 = Lanjut Kuliah
        if hasil == 0:
            st.error("⚠️ Mahasiswa terprediksi **Dropout**.", icon="🚨")
        elif hasil == 1:
            st.success("✅ Mahasiswa terprediksi **Lanjut Kuliah**.", icon="🎉")
        else:
            st.warning(f"❓ Hasil prediksi tidak dikenali: {hasil}", icon="⚠️")