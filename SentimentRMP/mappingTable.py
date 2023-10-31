# creates jaro winkler mapping table

import pandas as pd
from itertools import combinations
import jaro

idf = pd.read_csv(r'C:\Users\parki\Downloads\SentimentRMP\SentimentRMP\instructor.CSV')
idf_filtered = idf[idf['NumRatings'] > 0]
idf_filtered = idf_filtered.sort_values(by=['Name'])

similarity_threshold = 0.93

mapping_table = []

for (id1, name1), (id2, name2) in combinations(idf_filtered[['ID', 'Name']].itertuples(index = False), 2):
    similarity = jaro.jaro_winkler_metric(name1, name2)

    if similarity >= similarity_threshold:
        mapping_table.append((id1, name1, id2, name2, similarity))

mapping_df = pd.DataFrame(mapping_table, columns=['ID1', 'Name1', 'ID2', 'Name2', 'Similarity'])
mapping_df.to_csv('mapping_table2.csv', index=False)
