# student_performance_app.py

import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("student_performance_model.pkl")

# Define the Streamlit app
def main():
    st.title("Student Performance Prediction")
    st.write("Predict a student's final grade based on age, health, absences, and performance in previous exams.")

    # Create input fields
    age = st.number_input("Age", min_value=10, max_value=20, step=1)
    health = st.slider("Health (1 = very bad, 5 = very good)", 1, 5, step=1)
    absences = st.slider("Number of Absences", 0, 50, step=1)
    G1 = st.number_input("Grade in First Period Exam (0-20)", min_value=0, max_value=20)
    G2 = st.number_input("Grade in Second Period Exam (0-20)", min_value=0, max_value=20)

    # Predict button
    if st.button("Predict Performance"):
        # Prepare input data
        input_data = np.array([[age, health, absences, G1, G2]])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display prediction
        st.write(f"Predicted Final Grade (G3): {prediction[0]:.2f}")

# Run the app
if __name__ == '__main__':
    main()
        
