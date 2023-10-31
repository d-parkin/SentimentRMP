# converts xlsx to csv

import pandas as pd

# Specify the path to the XLSX file you want to convert
xlsx_file_path = 'C:\\Users\\parki\\Downloads\\SentimentRMP\\ratings.xlsx'

# Read the XLSX file into a DataFrame
df = pd.read_excel(xlsx_file_path)

# Specify the path where you want to save the CSV file
csv_file_path = 'ratings.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)
