import pandas as pd
from main.models import Patient

import os

def create_patients_from_csv(csv_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Iterate through the DataFrame and create Patient objects
    for index, row in df.iterrows():
        Patient.objects.create(
            gender=row['gender'],
            age=row['age'],
            hypertension=row['hypertension'],
            heart_disease=row['heart_disease'],
            ever_married=row['ever_married'],
            work_type=row['work_type'],
            Residence_type=row['Residence_type'],
            avg_glucose_level=row['avg_glucose_level'],
            bmi=row['bmi'],
            smoking_status=row['smoking_status'],
            stroke=row['stroke']
        )

if __name__ == "__main__":
    # Replace 'path_to_your_dataset.csv' with the actual path to your dataset
    # create_patients_from_csv('path_to_your_dataset.csv')
    print(os.getcwd())