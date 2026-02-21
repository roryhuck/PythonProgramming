## Python Programming
### Programming Assignemnt 5
#### By: Rory Huck 
import random      #importing random

trivia ={} # defining an empty dictionary 

with open('AnimalTrivia.txt') as f:  # opens the animal trivia test
    for line in f: #starts a loop
        line = line.strip() #gets rid of random spaces
        if line.startswith('#Q'):   # if the line starts with #Q gets rid of it
            q = line[2:].strip() 
            trivia[q] = {'a': '', 'c': []} #creates an entry
        elif line.startswith('^'): # if line starts with ^ then its the answer 
            trivia[q]['a'] = line[1:].strip()
        else:
            trivia[q]['c'].append(line) #otherwise its an option and gets appended

right = 0 #correct count
wrong = 0 #incorrect count

while input('Play some Triva? (yes/no): ').lower() == 'yes':    #starts game loop
    q = random.choice(list(trivia)) #picks random question
    print('\n' + q) #prints the question
    for choice in trivia[q]['c']: #prints the choices for that question
        print(choice)

    if input('Answer: ').lower() == trivia[q]['a'].lower(): #if answer is correct
        print('Correct!') #print correct
        right += 1 #update count
    else:
        print('Incorrect! Answer was:', trivia[q]['a']) #print incorrect
        wrong += 1 # update count

with open('TriviaResults.txt', 'a') as f: #opens a results file 
    f.write(f'Correct: {right}, Incorrect: {wrong}\n') #s

print('Done')