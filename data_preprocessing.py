# Fungsi preprocessing sesuai pipeline proyek ini
# Semua fitur sudah numerik, hanya lakukan scaling pada fitur numerik (selain kolom target 'Status')

import joblib
import pandas as pd

# Inisialisasi scaler (sudah di-fit pada data training)
scaler = joblib.load('scaler.joblib')

# Daftar fitur yang digunakan (berdasarkan file_context_0)
fitur = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Age_at_enrollment',
    'Debtor',
    'Scholarship_holder',
    'Tuition_fees_up_to_date',
    'Course',
    'Application_mode',
    'Previous_qualification'
    # Kolom 'Status' adalah target, tidak perlu di-preprocessing di sini
]

def data_preprocessing(df):
    # Pastikan hanya kolom fitur yang diproses (tanpa kolom target)
    X = df[fitur].copy()
    # Scaling seluruh fitur (karena semuanya numerik)
    X_scaled = scaler.transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=fitur, index=df.index)
    return X_scaled
