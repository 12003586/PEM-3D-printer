import string
import random

# Getting password length
length = 10

characterList = ""
characterList += string.ascii_letters
characterList += string.digits
characterList += string.punctuation
password = []

for i in range(length):
    # Picking a random character from our
    # character list
    randomchar = random.choice(characterList)

    # appending a random character to password
    password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))