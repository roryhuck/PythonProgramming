## Python Programming
### Programming Assignemnt 7
#### By: Rory Huck 
def feeding_tracker(feedings, mode='total'): #defining the function
    
    if mode == 'total': #check the total
        print('Total amount of food for each pet:')
        totals = {} #defining an empty dictionary 
        for pet in feedings: #loop through the pets
            total = 0
            for food in feedings[pet]: #loop food list
                total = total + food
            print('The total amount of food for the', pet, 'is', total) #print the results
            totals[pet] = total #save the total
        return totals

    elif mode == 'avg': #check the average
        print('Average amount of food for each pet')
        for pet in feedings: #loop through the pets
            total = 0
            count = 0
            for food in feedings[pet]: #loop through food list
                total = total + food #add items
                count = count + 1
            print('The average amount of food for the', pet, 'is', total/count) #print the average

    elif mode == 'most': #check most
        print('Most amount of food for each pet')
        for pet in feedings: #loop through the pets
            biggest = feedings[pet][0] #first element
            for food in feedings[pet]:#food loop
                if food > biggest:
                    biggest = food #compare/update 
            print('The most amount of food for the', pet, 'is', biggest)

    elif mode == 'least': #check the least
        print('Least amount of food for each pet')
        for pet in feedings: #loop through pets
            smallest = feedings[pet][0] #first element
            for food in feedings[pet]:
                if food < smallest:
                    smallest = food #compare/update
            print('The least amount of food for the', pet, 'is', smallest)

    elif mode == 'none': #check none
        print('No changes made') #no changes
        return feedings

    else:
        print('Invalid mode') #check if its valid
        return feedings
pets = {
    'horse': [4, 3, 4],
    'dog': [1, 2, 3],
    'cat' : [.5, 1, 1]
}

feeding_tracker(pets, 'total')
feeding_tracker(pets, 'avg')
feeding_tracker(pets, 'most')
feeding_tracker(pets, 'least')
feeding_tracker(pets, 'none')