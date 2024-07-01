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