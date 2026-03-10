## Python Programming
### Programming Assignemnt 6
#### By: Rory Huck 
import pandas as pd #imports Pandas
file_name = 'https://joannabieri.com/python/starbucks_drinkMenu_expanded.csv'
df = pd.read_csv(file_name) #reads in the file with the starbucks data 
df['Drink'] = df['Beverage'] + ' - ' + df['Beverage_prep'] #creates a new column drink 
categories = df['Beverage_category'].unique().tolist() #adds all unique beverage categories to a list 
columns = ['Calories', 'Sugars (g)', 'Protein (g) ', 'Caffeine (mg)', 'Total Fat (g)'] #defines a smaller list of columns to focus on

print('Beverage categories:', ', '.join(categories)) #prints out the possible categories to choose from
choice = input('Choose a beverage category: ').strip().lower()# asks for user imput on which category they want
category_map = {c.lower(): c for c in categories}# defines category map
if choice not in category_map: exit() #if they dont choose a know category it quits
choice = category_map[choice] #saves and prints out the imput choice
print(f'You chose: {choice}')

print('Nutrition columns:', ', '.join(columns)) #prints all nutrition columns the user can choose from
column = input('Choose a nutrition column: ').strip().lower() #asks for user imput
column_map = {c.lower(): c for c in columns}
if column not in column_map: exit() #is its not reconized it quits
column = column_map[column] #gets the column name

try:
    max_val = float(input(f'Enter maximum {column}: ')) #asks user for max
except: exit() #quit if not a number

filtered = df[(df['Beverage_category'] == choice) & (df[column] <= max_val)] #filters by chosen category and max value 

if len(filtered) == 0:
    print(f'No drinks under {max_val} {column} in {choice}.') #prints if no drinks match
else:
    filtered = filtered.sort_values(column) #sorts drinks by chosen column
    print(filtered[['Drink', column]]) #prints the filtered drinks with chosen colum
    if input('Save to my_drinks.csv? (yes/no): ').strip().lower() == 'yes':
        filtered.to_csv('my_drinks.csv', index=False)
        print('Saved')