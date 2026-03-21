## Python Programming
### Programming Assignemnt 8
#### By: Rory Huck 
##### I was having an issue with where the .txt file was saving on my computer and wasnt sure how to fix it 
def add_item(item): #defining add function
    f = open('bucket.txt', 'a') #open file 
    f.write(item + '\n') #write item
    f.close() #close the file

def remove_item(item): #function to remove items
    try: #read file
        f = open('bucket.txt', 'r') #open file
        lines = f.readlines() #read
        f.close() #close
    except:
        return

    new_list = [] #new list
    found = False

    for line in lines: #loop the lines
        if line.strip() == item: #check for match 
            found = True #mark found
        else:
            new_list.append(line)

    if found:
        f = open('bucket.txt', 'w') #open to write
        for line in new_list: #loop the new list
            f.write(line)
        f.close()
    else:
        print('item not found') 

def show_list(): #defing show function
    try:
        f = open('bucket.txt', 'r')
        for line in f: #loop for lines
            print(line.strip()) #print the lines 
        f.close()
    except:
        print('no list yet') 

# main
f = open('bucket.txt', 'a')  # open or create file
f.close()

while True: #continous loop unless quit 
    choice = input('add, remove, show, or quit: ') #user input

    if choice == 'add':
        item = input('enter item: ')
        add_item(item) 

    elif choice == 'remove':
        item = input('enter item to remove: ')
        remove_item(item)

    elif choice == 'show':
        show_list()

    elif choice == 'quit':
        break

    else:
        print('invalid choice')