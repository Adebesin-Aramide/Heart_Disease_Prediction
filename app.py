import streamlit as st
import numpy as np
from prediction import predict

def main():
    st.markdown('<h1 class="title">Heart Disease Prediction</h1>', unsafe_allow_html=True)
    st.write('Predict whether a patient has Heart Disease or not')

    st.markdown('<h5 class="title">Patient Diagnostic Features</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        sex = st.radio("Sex", ["Male", "Female"],
                      help='Select 1 out of 2 options for the sex ')
        cpt = st.radio("Chest Pain Type", ["Asymptomatic", "Atypical Angina", "Non Angina Pain", "Typical Angina"],
                      help='Select 1 out of 4 options for the chest pain type ')
        cholesterol = st.number_input(
            'Cholesterol', min_value=0, max_value=600, value=150)
        fbs = st.radio("Fasting Blood Sugar", ["Greater than 120", "Otherwise"],
                      help='Select 1 out of 2 options of the fasting blood sugar')

    with col2:
        exercise = st.radio("Exercise Angina", ["No", "Yes"],
                           help='Select 1 out of 2 options for exercise angina')
        old_peak = st.number_input(
            "Old Peak", min_value=-2.60, max_value=6.20, value=2.50)
        ST = st.radio("ST Slope", ["Downsloping", "Flat", "Upsloping"],
                      help='Select 1 out of 3 options of the ST slope')

    if st.button("Predict", key='predict_button'):
        result = predict(
            np.array([[sex, cpt, ST, fbs, exercise, cholesterol, old_peak]])
        )
        st.markdown('<div class="result">{}</div>'.format(result), unsafe_allow_html=True)

    st.markdown(
        '`Created by` Adebesin Aramide | 2023 | \
            `Code:` [GitHub](https://github.com/Adebesin-Aramide/Heart_Disease_Prediction/blob/main/Heart%20Disease%20Prediction.ipynb)'
    )

if __name__ == "__main__":
    main()