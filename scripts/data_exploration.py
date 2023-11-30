import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/healthcare-dataset-stroke-data.csv')

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Remove categorical columns and 'id' column
columns_to_remove = categorical_cols.union(['id'])
df = df.drop(columns=columns_to_remove)


pdf.head()

df.describe()

sns.countplot(x='stroke', data=df)
plt.title('Distribution to Stroke Cases')
plt.show()

sns.pairplot(df, hue='stroke')
plt.suptitle('PairPlot of Numerical Features', y=1.02)
plt.show()

corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()