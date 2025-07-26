import streamlit as st
import pandas as pd
import joblib

model = joblib.load("D:\Projects\Delivery On-Time Prediction ML Project\Delivery_On_Time_Prediction_ML_Project\Delivery_api\delivery_model.pkl")

st.title("📦 Delivery On-Time Predictor")

# User Inputs
warehouse = st.selectbox("Warehouse Block", ['F', 'A', 'B', 'C', 'D'])
mode = st.selectbox("Mode of Shipment", ['Flight', 'Ship', 'Road'])
calls = st.slider("Customer Care Calls", 1, 10, 3)
rating = st.slider("Customer Rating", 1, 5, 4)
cost = st.number_input("Cost of Product", value=200)
prior = st.number_input("Prior Purchases", value=2)
importance = st.selectbox("Product Importance", ['low', 'medium', 'high'])
discount = st.slider("Discount Offered", 0, 50, 10)
weight = st.number_input("Weight (grams)", value=1800)

# Prediction
if st.button("Predict"):
    df = pd.DataFrame({
        'Warehouse_block': [warehouse],
        'Mode_of_Shipment': [mode],
        'Customer_care_calls': [calls],
        'Customer_rating': [rating],
        'Cost_of_the_Product': [cost],
        'Prior_purchases': [prior],
        'Product_importance': [importance],
        'Discount_offered': [discount],
        'Weight_in_gms': [weight]
    })

    prediction = model.predict(df)
    st.success(f"🚀 Delivery Status: {'On Time' if prediction[0] == 1 else 'Late'}")
