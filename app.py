import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

model = joblib.load('model.pkl')  # Save your trained model as logistic_model.pkl

st.title('Titanic Survival Predictor')

pclass = st.number_input('Pclass', 1, 3, 1)
sex = st.selectbox('Sex', ['female', 'male'])
age = st.number_input('Age', 0, 100, 30)
sibsp = st.number_input('SibSp', 0, 10, 0)
parch = st.number_input('Parch', 0, 10, 0)
fare = st.number_input('Fare', 0.0, 600.0, 30.0)
embarked = st.selectbox('Embarked', ['S', 'C', 'Q'])

sex_map = {'female': 0, 'male': 1}
embarked_map = {'S': 2, 'C': 0, 'Q': 1}

input_data = np.array([[pclass, sex_map[sex], age, sibsp, parch, fare, embarked_map[embarked]]])
prediction = model.predict(input_data)[0]
probability = model.predict_proba(input_data)[0,1]

if st.button("🔍 Predict Survival"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("### 🧮 Prediction Result")
    if prediction == 1:
        st.success("✅ This passenger is predicted to **SURVIVE!**")
    else:
        st.error("❌ This passenger is predicted **NOT to survive.**")

    st.markdown(
        f"<p class='result'>Survival Probability: <b>{probability:.2%}</b></p>",
        unsafe_allow_html=True
    )

    # ====== Probability Bar ======
    st.progress(float(probability))

    # ====== Chart ======
    fig, ax = plt.subplots(figsize=(4, 0.6))
    ax.barh(["Survival Chance"], [probability], color="#00B4D8")
    ax.set_xlim(0, 1)
    ax.set_xlabel("Probability")
    st.pyplot(fig)