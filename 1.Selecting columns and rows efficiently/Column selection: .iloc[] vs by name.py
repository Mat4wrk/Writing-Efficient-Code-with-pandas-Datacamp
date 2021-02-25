# Use .iloc to select the first, fourth, fifth, seventh and eighth column and record the times before and after
iloc_start_time = time.time()
cols = poker_hands.iloc[:,[0,3,4,6,7]]
iloc_end_time = time.time()

# Print the time it took
print("Time using .iloc[] : {} sec".format(iloc_end_time - iloc_start_time))


# Use .iloc to select the first, fourth, fifth, seventh and eighth column and record the times before and after
iloc_start_time = time.time()
cols = poker_hands.iloc[:,[0,3,4,6,7]]
iloc_end_time = time.time()

# Print the time it took
print("Time using .iloc[] : {} sec".format(iloc_end_time - iloc_start_time))

# Use simple column selection to select the first, fourth, fifth, seventh and eighth column and record the times before and after
names_start_time = time.time()
cols = poker_hands[['S1', 'S2', 'R2', 'R3', 'S4']]
names_end_time = time.time()

# Print the time it took
print("Time using selection by name : {} sec".format(names_end_time - names_start_time))
