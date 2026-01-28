## Python Programming
### Programming Assignemnt 2
#### By: Rory Huck 
# lists of names, foods
first_names = [
    'Rory','Whitney','Yonte','Zoe','Mary','Kim','Jess','Sophie','Paige','Emma'
]

last_names = [
    'Huck','Farrell','Wickstrom','Klien','Smith','Clark','Patrick','Miles','Johnson','Adams'
]

foods = [ 
    'pasta','pizza','cookies','crackers','bananas','dates','apples','cheese','ice cream','cake'   
]
print("Length of first names list:", len(first_names))
print("Length of last names list:", len(last_names))
print("Length of products list:", len(foods))
# Creating email
for i in range(len(first_names)):
    first = first_names[i]
    last = last_names[i]
    food = foods[i]

    email = f'{first.lower()}.{last.lower()}@redlands.edu'

    print(f'To: {email}')
    print('Subject: Your Favorite Food from Trader Joe’s')
    print()
    print(f'Dear {first} {last},')
    print()
    print(
        f'I know that {food} is one of your favorite foods, '
        f'and I wanted to let you know that Trader Joe’s has '
        f'it back in stock.'
    )
    print()
    print(
        f'Next time you go to the store you should '
        f'check out their selection of {food} so you can stock up! '
    )
    print()
    print('Enjoy!')
    print('Kindly,') 
    print('Rory Huck')
    print('-' * 30)
    print()