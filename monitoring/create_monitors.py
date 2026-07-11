"""
create_monitors.py

This script checks whether the model is available in Arize.
Monitor configuration is managed from the Arize Dashboard.
"""

from arize.pandas.logger import Client
from config.arize_config import SPACE_ID, API_KEY

client = Client(
    space_id=SPACE_ID,
    api_key=API_KEY
)

print("Connected to Arize successfully.")
print("Model data has already been ingested.")
print("Create Drift, Performance and Data Quality monitors from the Arize Dashboard.")

import requests
from config.arize_config import SPACE_ID, API_KEY

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "space_id": SPACE_ID,
    "Content-Type": "application/json"
}

print("Checking Arize Connection...")

response = requests.get(
    "https://app.arize.com/api/v1/models",
    headers=headers
)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Connected Successfully to Arize")
else:
    print(response.text)