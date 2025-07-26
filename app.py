import streamlit as st
import pandas as pd
import joblib
import os

# Load the model safely
model_path = os.path.join("Delivery_api", "delivery_model.pkl")
model = joblib.load(model_path)

st.set_page_config(page_title="Delivery On-Time Predictor", page_icon="🚚", layout="centered")
st.title("📦 Delivery On-Time Predictor")

# Input features
warehouse = st.selectbox("Warehouse Block", ['F', 'A', 'B', 'C', 'D'])
mode = st.selectbox("Mode of Shipment", ['Flight', 'Ship', 'Road'])
calls = st.slider("Customer Care Calls", 1, 10, 3)
rating = st.slider("Customer Rating", 1, 5, 4)
cost = st.number_input("Cost of Product", value=200)
prior = st.number_input("Prior Purchases", value=2)
importance = st.selectbox("Product Importance", ['low', 'medium', 'high'])
gender = st.selectbox("Gender", ['M', 'F'])
discount = st.slider("Discount Offered (%)", 0, 50, 10)
weight = st.number_input("Weight (grams)", value=1800)

# Prediction
if st.button("Predict"):
    # Feature Engineering
    cost_rating_ratio = cost / rating if rating != 0 else 0
    volume_discount = (discount / cost) * 100 if cost != 0 else 0

    cluster = 0  

    # Create DataFrame
    input_df = pd.DataFrame([{
        'Warehouse_block': warehouse,
        'Mode_of_Shipment': mode,
        'Customer_care_calls': calls,
        'Customer_rating': rating,
        'Cost_of_the_Product': cost,
        'Prior_purchases': prior,
        'Product_importance': importance,
        'Gender': gender,
        'Discount_offered': discount,
        'Weight_in_gms': weight,
        'cost_rating_ratio': cost_rating_ratio,
        'volume_discount': volume_discount,
        'cluster': cluster
    }])

    # Encode categorical features manually
    mapping_dict = {
        'Warehouse_block': {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4},
        'Mode_of_Shipment': {'Flight': 0, 'Ship': 1, 'Road': 2},
        'Product_importance': {'low': 0, 'medium': 1, 'high': 2},
        'Gender': {'M': 0, 'F': 1}
    }

    for col in mapping_dict:
        input_df[col] = input_df[col].map(mapping_dict[col])

    # Predict
    prediction = model.predict(input_df)[0]
    result = "✅ On-Time Delivery" if prediction == 1 else "❌ Delayed Delivery"
    st.subheader("Prediction Result:")
    st.success(result)
