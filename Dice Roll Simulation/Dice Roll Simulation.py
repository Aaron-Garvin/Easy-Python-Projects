import random 
# Here we include random as it helps to pick a random number from a range

def roll_the_dice():
    return random.randint(1, 6)
# Here we Declared a roll_the_dice() function to use the random from the range 1 to 6

# Now we will declare our main() function

def main():
    print("Welcome to the Dice Roll Simulator!!!")
    while True: 
# This loop is infinte loops as the "True" is always True        
        user_input = input("Press 'r' to roll the dice or 'q' to quit: ").lower()
# Now we will take input from the user if He/She wants to roll a dice or not
# And we use .lower() function to make sure every character is in lower case for our condtions to be met        
        if user_input == 'r':
            print("You rolled: ",roll_the_dice())
# Now here we call our roll_the_dice() function to get a random number form 1 to 6            
        elif user_input == 'q':
            print("Thanks for playing!")
            break
# If user not want to continue then this infinte loop will get terminated because of the break statement        
        else:
            print("Invalid input. Please press 'r' to roll or 'q' to quit.")
main()
# Don't forget to call our main() function in the last