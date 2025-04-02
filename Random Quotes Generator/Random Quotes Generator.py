import random
# Here we import random module to provide the abilty of Randomization to the program
def get_random_quote():
# Declare a list of good quotes 
    quotes = [
        "The best way to predict the future is to invent it. - Alan Kay",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "Do what you can, with what you have, where you are. - Theodore Roosevelt",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "Be yourself; everyone else is already taken. - Oscar Wilde",
        "Hardest choices require the strongest wills. - thanos",
        "Let go your past cause it just doesn't matter the only thing matter what you choose to be now. - kung fu panda",
        "When it fell scary to jump that is exactly the moment you need to jump otherwise you will be in the same place in your whole life."
    ]
    return random.choice(quotes)
# Here we use random.choice() to get a random choice from the list name as quotes
# Display a random quote
print("Random Quote:")
print(get_random_quote())
