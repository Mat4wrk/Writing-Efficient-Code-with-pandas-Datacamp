# Replace the rank of the first three ranked names to 'MEDAL'
names.replace({'Rank': {1: 'MEDAL', 2: 'MEDAL', 3: 'MEDAL'}}, inplace=True)

# Replace the rank of the 4th and 5th ranked names to 'ALMOST MEDAL'
names.replace({'Rank': {4:'ALMOST MEDAL', 5:'ALMOST MEDAL'}}, inplace=True)
print(names.head())
