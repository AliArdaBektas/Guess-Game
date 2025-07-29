import random
number = random.randint(1,100)

guess = int(input("guess a number 1 to 100: "))
guess_right = 1

while guess != number:
    if guess > number:
        print("lower than guess")

    elif guess < number:
        print("higher than guess")

    guess = int(input("try to guess it again: "))

    guess_right += 1

print(f"congrats, {guess_right} times tried to guess")