import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report, confusion_matrix
import xgboost as xgb
import joblib
import os

class ModelTrainer:
    def __init__(self):
        self.models = {
            'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42),
            'XGBoost': xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
        }
        self.best_model = None
        self.best_model_name = ""
        self.best_score = 0
        
    def load_processed_data(self, filepath):
        print(f"Loading processed data from {filepath}...")
        df = pd.read_csv(filepath)
        return df
        
    def train_and_evaluate(self, df):
        # Separation
        X = df.drop(columns=['schedule_delay'])
        y = df['schedule_delay']
        
        # Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print(f"Training set size: {X_train.shape[0]}, Test set size: {X_test.shape[0]}")
        
        results = {}
        
        for name, model in self.models.items():
            print(f"\nTraining {name}...")
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else y_pred
            
            acc = accuracy_score(y_test, y_pred)
            prec = precision_score(y_test, y_pred)
            rec = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            auc = roc_auc_score(y_test, y_prob)
            
            print(f"--- {name} Results ---")
            print(f"Accuracy: {acc:.4f}")
            print(f"Precision: {prec:.4f}")
            print(f"Recall: {rec:.4f}")
            print(f"F1 Score: {f1:.4f}")
            print(f"ROC AUC: {auc:.4f}")
            
            results[name] = {'model': model, 'f1': f1, 'auc': auc}
            
            if f1 > self.best_score:
                self.best_score = f1
                self.best_model = model
                self.best_model_name = name
                
        print(f"\nBest Model: {self.best_model_name} with F1-Score: {self.best_score:.4f}")
        return X_test, y_test
        
    def plot_feature_importance(self, feature_names):
        if not self.best_model:
            print("No model trained yet.")
            return
            
        print(f"Plotting feature importance for {self.best_model_name}...")
        importances = self.best_model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        plt.figure(figsize=(10, 6))
        plt.title(f"Feature Importances ({self.best_model_name})")
        
        # Limit to top 20
        top_n = 20
        plt.bar(range(min(top_n, len(importances))), importances[indices][:top_n], align="center")
        plt.xticks(range(min(top_n, len(importances))), [feature_names[i] for i in indices[:top_n]], rotation=90)
        plt.tight_layout()
        plt.savefig('feature_importance.png')
        print("Feature importance plot saved to feature_importance.png")
        
    def save_best_model(self, output_dir='models'):
        os.makedirs(output_dir, exist_ok=True)
        if self.best_model:
            path = os.path.join(output_dir, f'best_model_{self.best_model_name}.pkl')
            joblib.dump(self.best_model, path)
            print(f"Saved best model to {path}")

if __name__ == "__main__":
    trainer = ModelTrainer()
    df = trainer.load_processed_data('dataset/projects_processed.csv')
    
    X_test, y_test = trainer.train_and_evaluate(df)
    
    # Feature names
    feature_names = df.drop(columns=['schedule_delay']).columns.tolist()
    trainer.plot_feature_importance(feature_names)
    
    trainer.save_best_model()
