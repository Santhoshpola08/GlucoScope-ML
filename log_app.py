# Stremlit Deployment as log-app.py

import streamlit as st
import numpy as np

model= joblib.load("logistic_model.pkl")

st.title("Diabetes Prediction")

preg= st.number_input("Pregnacies")
glucose= st.number_input("Glucose")
bp= st.number_input("Blood Pressure")
skin= st.number_input("Skin Thickness")
insulin= st.number_input("Insulin")
bmi= st.number_input("BMI")
dpf= st.number_input("Diabetes Pedigree Function")
age= st.number_input("Age")

if st.button("Predict"):
  features= np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
  pred= model.predict(features)[0]

  if pred==1:
    st.success(" The person is Diabetic")
  else:
    st.success("The person is not Diabetic")
