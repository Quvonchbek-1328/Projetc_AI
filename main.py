import os
import sys
from generate_dataset import generate_dataset
from preprocess_data import DataProcessor
from model_trainer import ModelTrainer

def run_pipeline():
    print("==================================================")
    print("   PROJECT RISK & DELAY OBSERVER - AI PIPELINE")
    print("==================================================")
    
    # Step 1: Data Generation
    print("\n[STEP 1] Generating Synthetic Dataset...")
    try:
        generate_dataset(num_rows=100000)
    except Exception as e:
        print(f"Error in generation: {e}")
        sys.exit(1)
        
    # Step 2: Preprocessing
    print("\n[STEP 2] Preprocessing Data...")
    try:
        dp = DataProcessor()
        df = dp.load_data('dataset/projects_dataset.csv')
        df_processed = dp.preprocess(df)
        df_processed.to_csv('dataset/projects_processed.csv', index=False)
        dp.save_processors()
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        sys.exit(1)
        
    # Step 3: Model Training & Evaluation
    print("\n[STEP 3] Model Training & Evaluation...")
    try:
        trainer = ModelTrainer()
        # Reload processed data to ensure it matches
        df = trainer.load_processed_data('dataset/projects_processed.csv')
        
        # Train
        X_test, y_test = trainer.train_and_evaluate(df)
        
        # Plot Importance
        feature_names = df.drop(columns=['schedule_delay']).columns.tolist()
        trainer.plot_feature_importance(feature_names)
        
        # Save Best Model
        trainer.save_best_model()
        
    except Exception as e:
        print(f"Error in model training: {e}")
        sys.exit(1)
        
    print("\n==================================================")
    print("   PIPELINE COMPLETED SUCCESSFULLY")
    print("==================================================")
    print(f"Best Model: {trainer.best_model_name} (F1: {trainer.best_score:.4f})")
    print("Artifacts saved: " + 
          "\n - dataset/projects_dataset.csv" +
          "\n - dataset/projects_processed.csv" +
          "\n - models/best_model_*.pkl" +
          "\n - models/*.pkl (scalers)" +
          "\n - feature_importance.png")

if __name__ == "__main__":
    run_pipeline()
