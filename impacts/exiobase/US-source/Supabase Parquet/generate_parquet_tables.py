import psycopg2
import os
import random
import string
import duckdb
import pandas as pd
from supabase import create_client, Client


# Replace with your actual API key and URL
supabase_url = "https://wovjoodfvamzysoxamdb.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indvdmpvb2RmdmFtenlzb3hhbWRiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE3NzQ1MDYsImV4cCI6MjAzNzM1MDUwNn0.hHM2aiNfHQe5Z9u-bKDYf7rImf4FnKCoMyoIc3j2uuk"

supabase: Client = create_client(supabase_url, supabase_key)
# Call the SQL function using the rpc method

# Call the custom function to get table names
response = supabase.rpc('get_table_names').execute()

# Print the table names
table_names = [table['table_name'] for table in response.data]


for table in table_names:
   result = supabase.table(table).select('*').execute()
   df = pd.DataFrame(result.data)
    
    # Save the DataFrame as a Parquet file
   df.to_parquet(f'./Tables/{table}.parquet', index=False)







