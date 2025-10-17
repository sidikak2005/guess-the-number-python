import random

print("Guess the Number Game")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

number = random.randint(1, 100)
attempts = 0

while True:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Try a higher number!")

    elif guess > number:
        print("Try a lower number!")

    else:
        print(f"Congratulations!! You guessed it in {attempts} attempts!")
        break

