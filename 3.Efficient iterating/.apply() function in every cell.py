# Define the lambda transformation
get_square = lambda x: x**2

# Apply the transformation
data_sum = poker_hands.apply(get_square)
print(data_sum.head())
