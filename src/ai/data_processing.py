# src/ai/data_processing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class DataProcessor:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)

    def handle_missing_values(self):
        self.data.fillna(self.data.mean(), inplace=True)  # Fill missing values with mean
        print("Missing values handled.")

    def normalize_data(self, numeric_features):
        scaler = StandardScaler()
        self.data[numeric_features] = scaler.fit_transform(self.data[numeric_features])
        print("Data normalized.")

    def encode_categorical_data(self, categorical_features):
        encoder = OneHotEncoder(sparse=False)
        encoded_features = encoder.fit_transform(self.data[categorical_features])
        encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_features))
        self.data = self.data.drop(categorical_features, axis=1)
        self.data = pd.concat([self.data, encoded_df], axis=1)
        print("Categorical data encoded.")

    def process_data(self, numeric_features, categorical_features):
        self.handle_missing_values()
        self.normalize_data(numeric_features)
        self.encode_categorical_data(categorical_features)
        print("Data processing complete.")

# Example usage
if __name__ == "__main__":
    processor = DataProcessor(data_path='data.csv')  # Specify your data file
    processor.process_data(numeric_features=['age', 'salary'], categorical_features=['gender', 'city'])
