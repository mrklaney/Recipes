import pandas as pd

#read a csv and make a dataframe called duplicateRowsDF
df = pd.read_csv('allrecipes.csv', encoding='latin1')


# !!!! this is the main line:    
#if use "subset" option can drop duplicates based on a particular column, like ingredient. Not done here

#result = df.drop_duplicates(keep='first')
result = df.drop_duplicates(keep='first', subset=['ingredient','summary','name'])

print('Result DataFrame:\n', result)

#write the csv file
result.to_csv('allrecipes_3.csv')

print(result.head())

print(result.count())
