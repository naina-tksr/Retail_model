import pandas as pd
import joblib

from database.database_connection import engine

# Read data from SQL View
query = "SELECT * FROM retail_view"

df = pd.read_sql(query, engine)

print("Total Records :", len(df))

print(df.head())

# Load Saved Model
model = joblib.load("models/saved_model.pkl")

# Select Features
X = df[["Quantity", "UnitPrice"]]

# Generate Predictions
predictions = model.predict(X)

# Add Prediction Column
df["Prediction"] = predictions

print("\nFirst 5 Predictions:")
print(df[["Quantity", "UnitPrice", "Prediction"]].head())

from arize.pandas.logger import Client
from arize.utils.types import Schema, ModelTypes, Environments

from config.arize_config import (
    SPACE_ID,
    API_KEY,
    MODEL_ID,
    MODEL_VERSION,
)

# Create Arize Client
client = Client(
    space_id=SPACE_ID,
    api_key=API_KEY
)

print("Client Created Successfully")

schema = Schema(
    prediction_id_column_name="InvoiceNo",
    feature_column_names=[
        "Quantity",
        "UnitPrice"
    ],
    prediction_label_column_name="Prediction"
)

print("SPACE_ID:", SPACE_ID)
print("MODEL_ID:", MODEL_ID)
print("MODEL_VERSION:", MODEL_VERSION)

response = client.log(
    dataframe=df,
    model_id=MODEL_ID,
    model_version=MODEL_VERSION,
    model_type=ModelTypes.REGRESSION,
    environment=Environments.PRODUCTION,
    schema=schema,
)

print(response)


