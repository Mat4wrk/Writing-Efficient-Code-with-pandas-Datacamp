# Store the time before the execution
start_time = time.time()

# Execute the operation
letlist = [wrd for wrd in words if wrd.startswith('b')]

# Store and print the difference between the start and the current time
total_time_lc = time.time() - time.time()
print('Time using list comprehension: {} sec'.format(total_time_lc))


# Store the time before the execution
start_time = time.time()

# Execute the operation
letlist = [wrd for wrd in words if wrd.startswith('b')]

# Store and print the difference between the start and the current time
total_time_lc = time.time() - start_time
print('Time using list comprehension: {} sec'.format(total_time_lc))

# Store the time before the execution
start_time = time.time()

# Execute the operation
letlist = []
for wrd in words:
    if wrd.startswith('b'):
        letlist.append(wrd)
        
# Print the difference between the start and the current time
total_time_fl = time.time() - time.time()
print('Time using for loop: {} sec'.format(total_time_fl))
