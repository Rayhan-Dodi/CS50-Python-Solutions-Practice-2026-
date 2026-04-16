import random

# Get level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# Generate number
number = random.randint(1, level)

# Guess loop
while True:
    try:
        guess = int(input("Guess: "))

        if guess <= 0:
            continue

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break

    except ValueError:
        continue
