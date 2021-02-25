zscore = lambda x: (x - x.mean()) / x.std()

# Apply the transformation
poker_trans = poker_grouped.transform(zscore)
print(poker_trans.head())


zscore = lambda x: (x - x.mean()) / x.std()

# Apply the transformation
poker_trans = poker_grouped.transform(zscore)

# Re-group the grouped object and print each group's means and standard deviation
poker_regrouped = poker_trans.groupby(poker_hands['Class'])

print(np.round(poker_regrouped.mean(), 3))
print(poker_regrouped.std())
