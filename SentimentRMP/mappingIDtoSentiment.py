# changes professorID in final sentiment table based on final mapping table

import pandas as pd

df = pd.read_csv(r'C:\Users\parki\Downloads\SentimentRMP\FINALLev0.8Jaro0.93.csv')
df2 = pd.read_csv(r'C:\Users\parki\Downloads\SentimentRMP\Ratings+Sentiment.csv')

for i in df.iterrows():
    print(i)
    # get ID2 for one row in df
    id2 = df.at[0, 'ID2']
    # get ID1 for the same row in df
    id1 = df.at[0, 'ID1']
    # for every row in df2 replace all ID2s with ID1
    for index, row in df.iterrows():
        id2 = row['ID2']
        id1 = row['ID1']
        
        # Replace 'InstructorID' values in df2 based on matching conditions
        df2['InstructorID'] = df2['InstructorID'].replace(id2, id1)

# produce new csv
df2.to_csv('Ratings+Sentiment+Mapping.csv', index=False)