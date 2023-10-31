# extracts mysql table to xlsx

import pandas as pd
from sqlalchemy import create_engine

password = 'zip@zap'
# Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine(f'mysql://root:zip@localhost/sentimentrmp')

# Specify the SQL query to fetch data from the database
sql_query = 'SELECT * FROM rating'

# Read data from the MySQL database into a pandas DataFrame
df = pd.read_sql_query(sql_query, con=engine)

# Specify the XLSX file path where you want to export the data
xlsx_file_path = 'ratings.xlsx'

# Export the data to an XLSX file
df.to_excel(xlsx_file_path, index=False, engine='openpyxl')

