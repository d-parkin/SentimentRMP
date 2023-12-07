# changes all spellings of 'Computer Science" to just "Computer Science"

import pandas as pd

df_initial = pd.read_csv(r'C:\Users\parki\Downloads\SentimentRMP\SentimentRMP\FINALTablewithDepartmentCollege.csv')

df_initial.loc[df_initial["Department"].isin(["Computer Science", "Computer Engineering amp Computer Science", "Computer Engineering & Computer Science", "Computer Engineering  Computer Science", "Computer Engineering"]) | df_initial["Course"].str.startswith("CE"), "Department"] = "Computer Engineering Computer Science"


# produce new csv
df_initial.to_csv('FINALcombinedCECS.csv', index=False)