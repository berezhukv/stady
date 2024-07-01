# ----------------------------------    Перше завдання    ----------------------------------

import string
import random

length = int(input("Enter the desired password length: "))

if length <= 0:
        print("It is not correct! Password cannot be 0 or a negative number")

print("Select options to generate a password:")
print("1 - lowercase")
print("2 - uppercase")
print("3 - digits")
print("4 - punctuation")
print("Or to select multiple options at once, enter a combination (for example, 124 for lowercase and uppercase letters and punctuation)")

choice = input("Your choice: ")

use_lowercase = '1' in choice
use_uppercase = '2' in choice
use_digits = '3' in choice
use_punctuation = '4' in choice

user_choice = ""
if use_lowercase:
    user_choice += string.ascii_lowercase
if use_uppercase:
    user_choice += string.ascii_uppercase
if use_digits:
    user_choice += string.digits
if use_punctuation:
    user_choice += string.punctuation

if not user_choice:
    print("You did not select any options. Please try again.")

else:
    password = ''.join(random.choice(user_choice) for _ in range(length))

    print(f"Згенерований пароль: {password}")

# ----------------------------------    Друге завдання    ----------------------------------

"""

import random

secret_number = random.randint(1, 100)
tries = 0

print("Hello, I have guessed a number from 1 to 100. Try to guess it.")

while True:
    guess = int(input("Enter your number: "))
    tries += 1

    if guess < secret_number:
        print("The secret number is bigger.")
    elif guess > secret_number:
        print("The secret number is lower.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {tries} tries(s).")

"""