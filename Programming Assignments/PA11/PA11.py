## Python Programming
### Programming Assignemnt 11
#### By: Rory Huck
# class for player 
class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def throw(self):
        options = ["ROCK", "PAPER", "SCISSORS"]
        
        while True:
            choice = input(f"{self.name}, choose ROCK, PAPER, or SCISSORS: ").upper()
            if choice in options:
                self.choice = choice
                break
            else:
                print("Invalid choice, try again.")

    def win(self):
        print(f"{self.name} wins!")

    def lose(self):
        print(f"{self.name} loses.")


# function to compare
def compare(player1, player2):
    if player1.choice == "ROCK" and player2.choice == "SCISSORS":
        player1.win()
        player2.lose()
    elif player1.choice == "SCISSORS" and player2.choice == "PAPER":
        player1.win()
        player2.lose()
    elif player1.choice == "PAPER" and player2.choice == "ROCK":
        player1.win()
        player2.lose()
    else:
        player2.win()
        player1.lose()


# game function
def play_game(player1, player2):
    player1.throw()

    # Clear screen
    print("\n" * 25)

    player2.throw()

    print("\n Results ")
    print(f"{player1.name} chose {player1.choice}")
    print(f"{player2.name} chose {player2.choice}")

    if player1.choice == player2.choice:
        print("It's a tie!")
    else:
        compare(player1, player2)


# Main code
name1 = input("Player 1 name: ")
name2 = input("Player 2 name: ")

player1 = Player(name1)
player2 = Player(name2)

play_game(player1, player2)