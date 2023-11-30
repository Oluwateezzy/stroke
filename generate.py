import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    'age': np.random.randint(18, 80, size=2000),
    'hypertension': np.random.choice([0, 1], size=2000),
    'heart_disease': np.random.choice([0, 1], size=2000),
    'average_glucose_level': np.random.uniform(70, 200, size=2000),
    'bmi': np.random.uniform(18.5, 40, size=2000),
    'stroke': np.random.choice([0, 1], size=2000)
}

df = pd.DataFrame(data)

df.to_csv('data/raw_data.csv', index=False)