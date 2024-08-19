import os
import random
import string
import duckdb
import pandas as pd

# Set the path for the new text file inside the Tables folder
#file_path = os.path.join(os.path.dirname(__file__), 'Tables', 'sample_data.txt')




conn = duckdb.connect('./US-2020-17schema.duckdb')

tables = conn.execute("SHOW TABLES").fetchdf()
table_names = tables['name'].tolist()

for table in table_names:
   result = conn.execute(f'SELECT * FROM {table}').fetchdf()
   result.to_parquet(f'./Tables/{table}.parquet', index=False)
   
   







