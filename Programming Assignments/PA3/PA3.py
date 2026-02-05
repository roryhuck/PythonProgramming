## Python Programming
### Programming Assignemnt 3
#### By: Rory Huck 
# Current names/ages
current_names = ['Rory', 'Whitney', 'Zoe']
current_ages = [19, 21, 22]

# New names/ages
new_names = ['Rory', 'Bella', 'Mary', 'Sarah', 'Jess']
new_ages = [19, 18, 30, 34, 32]

# Empty list to store emails
emails = []

# Loop
for i in range(len(new_names)):
    name = new_names[i]
    age = new_ages[i]

    # Check if they are already on the list
    if name in current_names:
        message = (
            f"Hello {name},\n"
            "You are already on the list!\n")
        print(message)
        emails.append(message)

    else:
        # Check age
        if age >= 21:
            current_names.append(name)
            current_ages.append(age)

            message = (
                f"Hello {name},\n"
                "You have been added to the list!\n")
            print(message)
            emails.append(message)

        else:
            message = (
                f"Hello {name},\n"
                "You must be over 21 to join the list.\n")
            print(message)
            emails.append(message)
print('---------------')
print("Updated Current Names:", current_names)
print("Updated Current Ages:", current_ages)