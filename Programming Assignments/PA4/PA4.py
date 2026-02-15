## Python Programming
### Programming Assignemnt 4
#### By: Rory Huck 
# Importing random for game
import random
#Defining my dictionary of animals including their clues
my_animals = {
    'dog': ['Barks', 'Normal pet'],
    'cat': ['Meows', 'Common pet'],
    'horse': ['Neighs', 'Lives in a barn'],
    'bird': ['Chirps', 'Has a beak']
}
#printing the name of the game and the rules
print('Animal Guessing Game')
print('Rules:')
print('- You will get clues about an animal')
print('- You have 3 guesses')
print("- Type 'quit' to stop\n")
#user input
play = input('Want to play? (yes/no): ')
#starting the game
if play == 'yes':

    secret_animal = random.choice(list(my_animals.keys()))#choosing a rancom secret animal and naming it
    clues = my_animals[secret_animal]#grabing the clues and defining them

    guesses = 0
    max_guesses = 3#max amount of guesses
    guessed_animal = []

    while guesses < max_guesses:#while statement so they cant go over the max guess

        print('\nClue:', clues[guesses % len(clues)])#uses mod to cycle through the 2 clues i have given

        guess = input('Guess (or quit): ')#user input and the four possible outputs

        if guess == 'quit': 
            print('You quit the game.')
            break

        if guess in guessed_animal:
            print('You already guessed that!')
            continue

        guessed_animal.append(guess)#adds animal to the list of guessed animals so they cant guess the same thing twice
        guesses += 1

        if guess.lower() == secret_animal:
            print('Correct! You win!')
            break
        else:
            print('Wrong!')

    if guess != secret_animal:
        print('Game over! The animal was:', secret_animal)

else:
    print('Maybe next time.')