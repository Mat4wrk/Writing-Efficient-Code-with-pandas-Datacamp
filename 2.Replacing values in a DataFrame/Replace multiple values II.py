start_time = time.time()

# Replace ethnicities as instructed
names['Ethnicity'].replace(['ASIAN AND PACI','BLACK NON HISP', 'WHITE NON HISP'], ['ASIAN AND PACIFIC ISLANDER','BLACK NON HISPANIC','WHITE NON HISPANIC'], inplace=True)

print("Time using .replace(): {} sec".format(time.time() - start_time))
