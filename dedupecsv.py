import pandas as pd
import datetime

#read a csv and make a dataframe called duplicateRowsDF
df = pd.read_csv('allrecipes.csv', encoding='latin1')


# !!!! this is the main line:    Drop duplicates based on a particular column, ingredient
result = df.drop_duplicates(keep='first')
print('Result DataFrame:\n', result)

#write the csv file
result.to_csv('allrecipes_2.csv')

print(result.head())
print(result.count())
