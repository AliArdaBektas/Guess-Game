import random
number = random.randint(1,100)

guess = int(input("guess a number 1 to 100: "))
guess_count = 1
guess_limit = 10
while guess != number:
    guess_limit -= 1
    if guess_limit == 0:
        print("you lost " + str(guess_count) + " times tried")
        break
    if guess > number:
        print("higher than number, you have " + str(guess_limit) + " guess left:")

    elif guess < number:
        print("lower than number, you have " + str(guess_limit) + " guess left:")

    guess = int(input("try to guess it again: "))

    guess_count += 1
else:
    print(f"congrats, {guess_count} times tried to guess")