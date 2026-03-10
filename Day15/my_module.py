# This module contains functions for Day 15 Intro to Python

# Hello world function
def hello_world():
    '''Prints hello world.'''
    print('Hello, world!')
    

def make_email(first,last):
    '''Creates an email address for first last'''
    my_email = f'{first.lower()}_{last.lower()}@redlands.edu'
    return my_email

def advertize_products(first,last,*products):
    '''Writes an email to first middle last advertizing the products.'''
    email = make_email(first,last)
    print(f'TO: {email}')

    print(f'\nDear {first} {last}')
        
    message = 'We are having a HUGE SALE! Come on down and check out our:'
    for product in products:
        message += f'\n    {product}'
        
    print(message)
    print('Sincerely, The Best Store')
    

    
    
    