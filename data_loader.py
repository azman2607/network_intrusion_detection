import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_data(file_path='data/house_data.csv'):
    df = pd.read_csv(file_path)
    df['society'].fillna('Unknown', inplace=True)
    df['balcony'].fillna(0, inplace=True)
    df['BHK'] = df['size'].apply(lambda x: int(x.split(' ')[0]))
    le_area = LabelEncoder()
    le_location = LabelEncoder()
    df['area_type'] = le_area.fit_transform(df['area_type'])
    df['location'] = le_location.fit_transform(df['location'])
    X = df[['area_type','location','total_sqft','bath','balcony','BHK']]
    y = df['price']
    return train_test_split(X, y, test_size=0.2, random_state=42), le_area, le_location