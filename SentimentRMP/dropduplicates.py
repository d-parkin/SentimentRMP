# drop duplicates from combined jaro winkler and levenschtein mapping tables

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('SentimentRMP/Lev0.8Jaro0.93.csv')

# Remove duplicate rows based on 'id1' and 'id2'
df = df.drop_duplicates(subset=['ID1', 'ID2'])

# Save the DataFrame to a new CSV file without duplicates
df.to_csv('Lev0.8Jaro0.93final.csv', index=False)
