import streamlit as st
from src.predictor import predict_price

st.title('🏡 House Price Prediction App')

area_type = st.selectbox('Area Type', ['Super built-up Area','Plot Area','Built-up Area'])
location = st.selectbox('Location', ['Electronic City Phase II','Chikka Tirupathi','Uttarahalli','Lingadheeranahalli','Kothanur','Whitefield','Old Airport Road'])
total_sqft = st.number_input('Total Square Feet', min_value=300, max_value=10000, value=1000)
bath = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)
balcony = st.number_input('Number of Balconies', min_value=0, max_value=5, value=1)
BHK = st.number_input('Number of Bedrooms (BHK)', min_value=1, max_value=5, value=2)

if st.button('Predict Price'):
    price = predict_price(area_type, location, total_sqft, bath, balcony, BHK)
    st.success(f'Predicted House Price: ₹ {round(price, 2)} Lakhs')