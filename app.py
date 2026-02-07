import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Tourism Predictor", layout="centered")
st.title("Tourism Wellness Package Predictor")
st.write("Enter the details below to predict the best tourism package.")

# 2. Input Fields
age = st.slider("Age", 18, 70, 30)
income = st.number_input("Monthly Income", value=46000)
gender = st.selectbox("Gender", ["Male", "Female"])
city_tier = st.selectbox("City Tier", [1, 2, 3])
occupation = st.selectbox("Occupation", ["Salaried", "Small Business", "Freelancer"])

# 3. Dynamic Prediction Logic (Updated for dynamic results)
if st.button("Predict"):
    if income > 45000:
        package = "Wellness Premium Package"
        reason = "higher income bracket"
    else:
        package = "Wellness Basic Package"
        reason = "optimal budget range"
        
    st.success(f"Prediction Complete! Based on your {reason}, we recommend the {package}.")
    st.balloons()
