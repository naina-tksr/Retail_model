import pandas as pd
from database.database_connection import engine

query = "SELECT * FROM retail_view LIMIT 5"

df = pd.read_sql(query, engine)

print(df)