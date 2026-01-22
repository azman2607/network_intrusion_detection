import joblib
import pandas as pd

def predict_price(area_type, location, total_sqft, bath, balcony, BHK):
    model = joblib.load('house_price_model.pkl')
    le_area = joblib.load('le_area.pkl')
    le_location = joblib.load('le_location.pkl')
    area_type_encoded = le_area.transform([area_type])[0]
    location_encoded = le_location.transform([location])[0]
    data = pd.DataFrame([[area_type_encoded, location_encoded, total_sqft, bath, balcony, BHK]],
                        columns=['area_type','location','total_sqft','bath','balcony','BHK'])
    return model.predict(data)[0]

if __name__ == '__main__':
    price = predict_price('Super built-up Area', 'Whitefield', 1170, 2, 1, 2)
    print(f'Predicted Price: {price} Lakhs')