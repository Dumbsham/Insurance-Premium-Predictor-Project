import streamlit as st
import pandas as pd
import pickle

# 1. Load the saved model and scaler
import os

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths to models
model_path = os.path.join(project_root, 'models', 'model.pkl')
scaler_path = os.path.join(project_root, 'models', 'scaler.pkl')

# Load models
with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)
# 2. App Title and Description
st.title("🏥 Insurance Premium Predictor")
st.write("Enter your details below to get an estimated insurance charge.")

# 3. Create Input Fields for the User
# We need inputs for: age, sex, bmi, children, smoker, region
c1, c2 = st.columns(2)

with c1:
    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    sex = st.selectbox("Sex", ["Male", "Female"])
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

with c2:
    children = st.number_input("Children", min_value=0, max_value=10, value=0)
    smoker = st.selectbox("Smoker", ["No", "Yes"])
    region = st.selectbox("Region", ["southeast", "northwest", "southwest", "northeast"])

# 4. Preprocess Input (Match the logic from your training script)

# Map categorical inputs to numbers
is_female = 1 if sex == "Female" else 0
is_smoker = 1 if smoker == "Yes" else 0

# Handle Region (Your model uses 'region_southeast' and 'region_northwest')
region_southeast = 1 if region == "southeast" else 0
region_northwest = 1 if region == "northwest" else 0

# Handle BMI Category (Your model uses 'bmi_category_Obese')
# Logic: If BMI >= 30, it is Obese
bmi_category_Obese = 1 if bmi >= 30 else 0

# 5. Create a DataFrame for the model
# IMPORTANT: The columns must differ EXACTLY in name and order as your training X
input_data = pd.DataFrame({
    'age': [age],
    'is_female': [is_female],
    'bmi': [bmi],
    'children': [children],
    'is_smoker': [is_smoker],
    'region_southeast': [region_southeast],
    'bmi_category_Obese': [bmi_category_Obese],
    'region_northwest': [region_northwest]
})

# 6. Scale the numerical columns
# Your training script scaled: 'age', 'bmi', 'children'
cols_to_scale = ['age', 'bmi', 'children']
input_data[cols_to_scale] = scaler.transform(input_data[cols_to_scale])

# 7. Prediction Button
if st.button("Calculate Premium"):
    prediction = model.predict(input_data)
    result = round(prediction[0], 2)
    
    st.success(f"Estimated Insurance Charge: ${result}")
    
    # Optional: Show the processed data for debugging
    # st.write(input_data)