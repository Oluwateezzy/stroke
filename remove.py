import pandas as pd

# Load the dataset
df = pd.read_csv('data/healthcare-dataset-stroke-data.csv')  # Replace 'your_dataset.csv' with your actual file path

# Display the original dataset
print("Original dataset:")
print(df)

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Remove categorical columns and 'id' column
columns_to_remove = categorical_cols.union(['id'])
df = df.drop(columns=columns_to_remove)

# Display the dataset after removing categorical variables
print("\nDataset after removing categorical variables:")
print(df)
