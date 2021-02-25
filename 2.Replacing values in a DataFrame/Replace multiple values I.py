start_time = time.time()

# Replace all non-Hispanic ethnicities with 'NON HISPANIC'
names['Ethnicity'].loc[(names["Ethnicity"] == 'BLACK NON HISPANIC') | 
                      (names["Ethnicity"] == 'BLACK NON HISP') | 
                      (names["Ethnicity"] == 'WHITE NON HISPANIC') | 
                      (names["Ethnicity"] == 'WHITE NON HISP')] = 'NON HISPANIC'

print("Time using .loc[]: sec".format(time.time() - start_time))


start_time = time.time()

# Replace all non-Hispanic ethnicities with 'NON HISPANIC'
names['Ethnicity'].replace(['BLACK NON HISP', 'BLACK NON HISPANIC', 'WHITE NON HISP' , 'WHITE NON HISPANIC'], 'NON HISPANIC', inplace=True)

print("Time using .replace(): {} sec".format(time.time() - start_time))
