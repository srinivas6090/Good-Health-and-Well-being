import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

def preprocess_data(df):
    # Specify numeric and categorical columns
    numeric_cols = ['Age', 'BMI', 'BloodPressure', 'Cholesterol']
    categorical_cols = ['Gender', 'SmokingStatus']
    
    # Handle missing values for numeric columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    # Fill missing values in categorical columns (if any) with mode
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])  # Assign filled values back to the column
    
    # Standardize numerical features
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # Convert categorical columns to dummy variables
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    return df

# Sample usage
df = pd.read_csv('data/raw/health_data.csv')
df = preprocess_data(df)

# Save the processed DataFrame to a CSV file
output_dir = 'data/processed'
os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
processed_file_path = os.path.join(output_dir, 'processed_health_data.csv')
df.to_csv(processed_file_path, index=False)

print(f"Processed data saved to {processed_file_path}")

# Optionally, split the data into features and target variable
X, y = df.drop('ChronicDiseases', axis=1), df['ChronicDiseases']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
