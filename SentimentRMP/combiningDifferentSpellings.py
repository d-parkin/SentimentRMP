# changes all spellings of 'Computer Science" to just "Computer Science"

import pandas as pd

df_initial = pd.read_csv(r'C:\Users\david\OneDrive\Documents\GitHub\SentimentRMP\SentimentRMP\FINALTablewithDepartmentCollege.csv')

for index, row in df_initial.iterrows():
    if row["Department"] == "Computer Science" or "Computer Engineering amp Computer Science" or "Computer Engineering & Computer Science" or "Computer Engineering  Computer Science" or "Computer Engineering" or "Computer Science" or "Computer Engineering amp Computer Science" or "Computer Engineering & Computer Science" or "Computer Engineering  Computer Science" or "Computer Engineering":
        df_initial.at[index, "Department"] = "Computer Engineering Computer Science"

# produce new csv
df_initial.to_csv('FINALcombinedCECS.csv', index=False)