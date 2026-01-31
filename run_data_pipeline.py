import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation

if __name__ == '__main__':
    # Simple data ingestion without importing the full class
    print("Starting data ingestion...")
    df = pd.read_csv('notebook/data/stud.csv')
    os.makedirs('artifacts', exist_ok=True)
    df.to_csv('artifacts/data.csv', index=False)
    train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
    train_set.to_csv('artifacts/train.csv', index=False)
    test_set.to_csv('artifacts/test.csv', index=False)
    print("Data ingestion completed.")
    
    # Run data transformation
    print("\nStarting data transformation...")
    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
        'artifacts/train.csv', 'artifacts/test.csv'
    )
    print(f"Data transformation completed. Preprocessor saved at: {preprocessor_path}")
    print("Pipeline completed successfully!")
