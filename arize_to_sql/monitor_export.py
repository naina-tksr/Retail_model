import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# MySQL Connection
engine = create_engine(
    "mysql+pymysql://root:root@localhost/retaildb"
)

# Sample monitor data
monitor_data = pd.DataFrame({
    "model_id": ["Retail_Sales_Model"],
    "monitor_name": ["Retail Monitor"],
    "monitor_type": ["Data Quality"],
    "status": ["Healthy"],
    "records_processed": [20000],
    "created_time": [datetime.now()]
})

# Save to SQL
monitor_data.to_sql(
    "arize_monitor_data",
    engine,
    if_exists="replace",
    index=False
)

print("Monitor data exported successfully to SQL.")