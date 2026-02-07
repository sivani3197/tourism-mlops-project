import streamlit as st
import pandas as pd

st.title("Visit with Us: Package Predictor")
st.write("Predicting if a customer will buy the Wellness Tourism Package.")

age = st.number_input("Customer Age", 18, 100, 30)
income = st.number_input("Monthly Income", value=25000)
passport = st.selectbox("Has Passport? (1=Yes, 0=No)", [0, 1])

if st.button("Predict"):
    # this will be connected to the registered model
    st.success("The model predicts this customer IS likely to buy!")

# The Docker Instructions
%%writefile tourism_project/deployment/Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

#The Library List
%%writefile tourism_project/deployment/requirements.txt
streamlit
pandas
scikit-learn
numpy
