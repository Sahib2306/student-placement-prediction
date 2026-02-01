import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🎓 Student Placement Prediction")
st.write("Predict placement using IQ, CGPA, and Backlogs")

# Input fields
iq = st.number_input("IQ", min_value=50, max_value=200, value=110)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1, value=6.5)
backlogs = st.number_input("Backlogs", min_value=0, max_value=10, value=0)

# Predict button
if st.button("Predict Placement"):
    input_data = np.array([[iq, cgpa, backlogs]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Placement: YES")
    else:
        st.error("❌ Placement: NO")
