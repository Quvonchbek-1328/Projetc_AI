import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os

class DataProcessor:
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.numeric_cols = []
        self.categorical_cols = []
        
    def load_data(self, filepath):
        print(f"Loading data from {filepath}...")
        df = pd.read_csv(filepath)
        return df
        
    def preprocess(self, df):
        print("Preprocessing data...")
        df_clean = df.copy()
        
        # 1. Drop identifiers and text heavy fields
        drop_cols = ['project_id', 'project_name', 'organization_name', 'scope_description', 
                     'out_of_scope', 'project_goal', 'key_deliverables', 'project_manager_name',
                     'country', 'region', 'project_language', 'tools_used', 'start_date', 'end_date']
        
        # Keep start_date/end_date for duration calc if needed, but we have duration_days
        # Let's drop them for the model to keep it simple, strictly using features
        df_clean = df_clean.drop(columns=[col for col in drop_cols if col in df_clean.columns])
        
        # 2. Handle Categorical
        self.categorical_cols = df_clean.select_dtypes(include=['object']).columns.tolist()
        print(f"Categorical columns: {self.categorical_cols}")
        
        for col in self.categorical_cols:
            le = LabelEncoder()
            df_clean[col] = le.fit_transform(df_clean[col].astype(str))
            self.label_encoders[col] = le
            
        # 3. Handle Numerical (Scale)
        self.numeric_cols = df_clean.select_dtypes(include=['int64', 'float64']).columns.tolist()
        # Remove target from scaling
        if 'schedule_delay' in self.numeric_cols:
            self.numeric_cols.remove('schedule_delay')
            
        print(f"Numerical columns to scale: {self.numeric_cols}")
        df_clean[self.numeric_cols] = self.scaler.fit_transform(df_clean[self.numeric_cols])
        
        return df_clean

    def save_processors(self, output_dir='models'):
        os.makedirs(output_dir, exist_ok=True)
        joblib.dump(self.label_encoders, os.path.join(output_dir, 'label_encoders.pkl'))
        joblib.dump(self.scaler, os.path.join(output_dir, 'scaler.pkl'))
        print("Processors saved.")

if __name__ == "__main__":
    dp = DataProcessor()
    df = dp.load_data('dataset/projects_dataset.csv')
    df_processed = dp.preprocess(df)
    
    # Save processed data
    df_processed.to_csv('dataset/projects_processed.csv', index=False)
    print("Processed data saved to dataset/projects_processed.csv")
