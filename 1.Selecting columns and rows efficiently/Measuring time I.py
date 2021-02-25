# Calculate the result of the problem using formula() and print the time required
N = 1000000
fm_start_time = time.time()
first_method =  formula(1000000)
print("Time using formula: {} sec".format(time.time() - fm_start_time))

# Calculate the result of the problem using brute_force() and print the time required
sm_start_time = time.time()
second_method = brute_force(1000000)
print("Time using the brute force: {} sec".format(time.time() - sm_start_time))
