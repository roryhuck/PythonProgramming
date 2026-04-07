## Python Programming
### Programming Assignemnt 10
#### By: Rory Huck 
#1
print(statesDF.columns)
print(povertyDF.columns)
print(statesDF.shape)
print(povertyDF.shape)
statesDF.info()
povertyDF.info()
statesDF.describe()
povertyDF.describe()
#  Question 1:
 #The states data frame has 52 rows and 3 columns and represents state boundaries. The poverty data frame has 100,682 rows and 9 columns and has detailed school data with locations and poverty measures. The summary statitics show that there is a wide varitey in poverty estimates across the U.S.
#2
statesDF.plot(column='NAME', legend=False, figsize=(10,6))
plt.title("U.S. States")
plt.show()
povertyDF.plot(column='IPR_EST',markersize=.5,
               figsize=(10,6),
               legend=True)

plt.title("School Poverty Estimates")
plt.show()
#3
statesDF = statesDF.to_crs(epsg=4326)
povertyDF = povertyDF.to_crs(epsg=4326)
joinDF = povertyDF.sjoin(statesDF)
stateDF = joinDF[joinDF['NAME_right'] == 'Colorado']
stateDF.plot(column='IPR_EST', markersize=10)
state_shape = statesDF[statesDF['NAME'] == 'Colorado']

ax = state_shape.boundary.plot()

stateDF.plot(ax=ax, column='IPR_EST', markersize=10)
#4
top10_poverty = stateDF.sort_values(by='IPR_EST', ascending=True).head(10)
print(top10_poverty[['NAME_left', 'IPR_EST']])
co_avg = stateDF['IPR_EST'].mean()
print(co_avg)
state_avgs = {}

for state in joinDF['NAME_right'].unique():
    temp = joinDF[joinDF['NAME_right'] == state]
    state_avgs[state] = temp['IPR_EST'].mean()

print(state_avgs)
print("Colorado avg:", state_avgs['Colorado'])
print("Overall avg:", sum(state_avgs.values())/len(state_avgs))
#Question 4: The top 10 highest poverty schools in Colorado are Irving Elementary (104) and Central High School (110) for the income to poverity ratio estimates. This is a measure of a housholds income and how it compares to the fedaeral poverty levels. These schools have incomes well below the poverty line based on their low IPR estimates. The average IPR estimate in Colorado is about 359 which is higherthan the overall U.S. average of 316.