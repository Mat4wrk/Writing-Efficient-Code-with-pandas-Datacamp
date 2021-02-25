# Replace the number rank by a string
names['Rank'].replace({1: 'FIRST', 2: 'SECOND', 3: 'THIRD'}, inplace=True)
print(names.head())
