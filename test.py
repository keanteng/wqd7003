import joblib
import pandas as pd

# Load the model
model = joblib.load('model/model.pkl')

# Load the data
data = pd.read_csv('data/sample_data.csv')

# Make predictions
predictions = model.predict(data)

# save the predictions
data['Churn'] = predictions

# save as sample_output.csv
data.to_csv('data/sample_output.csv', index=False)
