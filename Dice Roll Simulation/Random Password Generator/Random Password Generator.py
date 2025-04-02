import random
# Here we import random module to provide the ability of randomization to the program
import string
# Here we import string module to excess all the character set
def generate_password(length=12):
    characters = string.ascii_letters + string.digits +string.punctuation
    # Here we use string.(ascii_letters, .digits, .punctuation) to get all letters(Caps inculde), digits, and special character respectively
    password = ''.join(random.choice(characters) for _ in range(length))
    # Here random.choice() use to selects a random character from characters
    # Here for _ in range() use to repeats the selection process till the length of the password
    # Here ''.join() use to joins all randomly selected characters into a single string (without spaces or separators)
    return password

# The above function will generate a random password with uppercase, lowercase, digits, and special characters

# User input for password length
length = int(input("Enter password length : "))
password = generate_password(length)
print("Generated Password : ", password)
