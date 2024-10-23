# src/ai/predictive_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

class PredictiveModel:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.model = RandomForestClassifier()
        self.features = None
        self.target = None

    def preprocess_data(self):
        # Basic data preprocessing
        self.data.fillna(self.data.mean(), inplace=True)  # Handle missing values
        self.features = self.data.drop('target', axis=1)  # Assuming 'target' is the label column
        self.target = self.data['target']

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.features, self.target, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print("Model Accuracy:", accuracy_score(y_test, predictions))
        print("Classification Report:\n", classification_report(y_test, predictions))

    def save_model(self, filename='predictive_model.pkl'):
        joblib.dump(self.model, filename)
        print(f"Model saved to {filename}")

    def load_model(self, filename='predictive_model.pkl'):
        self.model = joblib.load(filename)
        print(f"Model loaded from {filename}")

# Example usage
if __name__ == "__main__":
    model = PredictiveModel(data_path='data.csv')  # Specify your data file
    model.preprocess_data()
    model.train_model()
    model.save_model()
