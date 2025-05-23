import streamlit as st
import pandas as pd
import joblib

def load_features(feature_path='features.txt'):
    with open(feature_path, 'r') as f:
        features = f.read().splitlines()
    return features

def preprocess_input(df_input, feature_names, scaler):
    # One-hot encode input (seperti saat training)
    df_encoded = pd.get_dummies(df_input, drop_first=True)

    # Reindex agar kolom sesuai fitur training, isi dengan 0 jika tidak ada
    df_encoded = df_encoded.reindex(columns=feature_names, fill_value=0)

    # Kolom numerik untuk scaler
    numeric_cols = df_encoded.select_dtypes(include=['int64', 'float64']).columns
    df_encoded[numeric_cols] = scaler.transform(df_encoded[numeric_cols])

    return df_encoded

@st.cache_resource(show_spinner=False)
def load_model_and_artifacts():
    model = joblib.load('model.joblib')
    scaler = joblib.load('scaler.pkl')
    features = load_features('features.txt')
    return model, scaler, features

def main():
    st.title("Prediction App dengan Streamlit")

    st.write("Upload file CSV yang akan diprediksi:")

    uploaded_file = st.file_uploader("Pilih file CSV", type=['csv'])
    if uploaded_file is not None:
        try:
            df_input = pd.read_csv(uploaded_file)
            st.write("Data input:")
            st.dataframe(df_input)

            model, scaler, features = load_model_and_artifacts()

            X_input = preprocess_input(df_input, features, scaler)

            preds = model.predict(X_input)

            if hasattr(model, 'predict_proba'):
                probs = model.predict_proba(X_input)
            else:
                probs = None

            df_result = df_input.copy()
            df_result['Prediction'] = preds
            if probs is not None:
                for i in range(probs.shape[1]):
                    df_result[f'Probability_{i}'] = probs[:, i]
            else:
                st.warning("Model tidak mendukung predict_proba, probabilitas tidak ditampilkan.")

            st.write("Hasil prediksi:")
            st.info("Geser ke kanan untuk melihat kolom Prediction dan Probability")
            st.dataframe(df_result)

        except Exception as e:
            st.error(f"Terjadi error saat preprocessing/prediksi: {e}")

if __name__ == "__main__":
    main()
