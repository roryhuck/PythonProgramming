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