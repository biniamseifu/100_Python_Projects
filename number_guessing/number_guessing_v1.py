import random

random_num = random.randint(1, 10)

while True:
    guess_num = int(input("Guess a number between (1 - 10): "))

    if guess_num > 10:
        print("Please Guess between (1 - 10)")
    elif guess_num > random_num:
        print("Too High")
    elif guess_num < random_num:
        print("Too Low")
    else:
        print(f"You Guess The Number {random_num} Correctly")
        break

