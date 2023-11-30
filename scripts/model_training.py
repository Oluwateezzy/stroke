import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from keras.models import Sequential
from keras.layers import Dense

# Load the dataset
df = pd.read_csv('data/healthcare-dataset-stroke-data.csv')

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Remove categorical columns and 'id' column
columns_to_remove = categorical_cols.union(['id'])
df = df.drop(columns=columns_to_remove)

# Separate features and target variable
x = df.drop('stroke', axis=1)
y = df['stroke']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)

# Standardize features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Build the neural network model
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=x_train.shape[1]))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))

# Predict probabilities for the test set
y_pred_probs = model.predict(x_test)

# Convert probabilities to binary labels using a threshold (0.5 in this case)
threshold = 0.5
y_pred = (y_pred_probs > threshold).astype(int)

# Print confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
