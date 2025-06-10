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

# Load model dan scaler yang sudah disimpan
model = joblib.load('model_prediksi.joblib')
scaler = joblib.load('scaler.joblib')



def predict_status(input_data):
    """
    input_data: DataFrame dengan kolom sesuai fitur
    return: label prediksi (string)
    """
    X = data_preprocessing(input_data)
    y_pred = model.predict(X)
    # Tidak ada proses encoding, langsung kembalikan hasil prediksi
    return y_pred[0]
