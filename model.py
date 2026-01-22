import joblib
from sklearn.ensemble import RandomForestRegressor
from src.data_loader import load_data

def train_model():
    (X_train, X_test, y_train, y_test), le_area, le_location = load_data()
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, 'house_price_model.pkl')
    joblib.dump(le_area, 'le_area.pkl')
    joblib.dump(le_location, 'le_location.pkl')
    print('Model training completed and saved!')

if __name__ == '__main__':
    train_model()