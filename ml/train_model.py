import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
data = pd.read_csv("ml/vehicle_dataset.csv")

# Convert text columns into numbers
fuel_encoder = LabelEncoder()
category_encoder = LabelEncoder()

data["Fuel_Type"] = fuel_encoder.fit_transform(data["Fuel_Type"])
data["Vehicle_Category"] = category_encoder.fit_transform(data["Vehicle_Category"])

# Select input features
X = data[["Engine_Size", "Horsepower", "Weight", "Doors", "Seats", "Fuel_Type"]]

# Select target column
y = data["Vehicle_Category"]

# Train the Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Save the trained model and encoders
joblib.dump(model, "ml/vehicle_model.pkl")
joblib.dump(fuel_encoder, "ml/fuel_encoder.pkl")
joblib.dump(category_encoder, "ml/category_encoder.pkl")

print("Model trained successfully!")
print("Files saved:")
print("- vehicle_model.pkl")
print("- fuel_encoder.pkl")
print("- category_encoder.pkl")