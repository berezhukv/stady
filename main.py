# ----------------------------------    HOME WORK 6       ----------------------------------
# ----------------------------------    Перше завдання    ----------------------------------

liste = [1, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]

positive = 0
negative = 0

for i in liste:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1

print(f"Кількість додатних елементів: {positive}")
print(f"Кількість від'ємних елементів: {negative}")

# ----------------------------------    Друге завдання    ----------------------------------

"""

liste = [1, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]

index_negative = -1

for index, i in enumerate(liste):
    if i < 0:
        index_negative = index
        break


if index_negative != -1:
    print(f"Перший від'ємний елемент: {liste[index_negative]}")
    print(f"Індекс першого від'ємного елемента: {index_negative}")
else:
    print("У списку немає від'ємних елементів.")

"""

# ----------------------------------    Третє завдання    ----------------------------------

"""

liste = [-6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]

index_positive = -1

for index, i in enumerate(liste):
    if i > 0:
        index_positive = index
        break


if index_positive != -1:
    print(f"Перший додатній елемент: {liste[index_positive]}")
    print(f"Індекс першого додатнього елемента: {index_positive}")
else:
    print("У списку немає додатніх елементів.")

"""

# ----------------------------------    Четверте завдання    ----------------------------------

"""

liste = [0, 0, 1, 4, 4, -6, -2, -6, 7]

index_negative = -1

for i in range(len(liste) -1, -1, -1):
    if liste[i] < 0:
        index_negative = i
        break


if index_negative != -1:
    print(f"Останній від'ємний елемент: {liste[index_negative]}")
    print(f"Індекс останнього від'ємного елемента: {index_negative}")
else:
    print("У списку немає від'ємних елементів.")

"""

# ----------------------------------    HOME WORK 5       ----------------------------------
# ----------------------------------    Перше завдання    ----------------------------------

"""

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

"""

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