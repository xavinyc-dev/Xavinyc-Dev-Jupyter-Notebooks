import random


secret_number = random.randint(1, 10)
num_of_guesses = 0
total_guesses = 5

while True:
    guess = (
        input(
            f"Guess the secret number from 1-10! You have {total_guesses} guess{'es' if total_guesses > 1 else ''}: "
        )
        .strip()
        .lower()
    )
    if guess == "exit":
        print("Thanks for playing!")
        break
    if not guess.isdigit():
        print("Thats an invalid digit. Try Again!")
        input("Press Enter to try again...")
        continue
    guess = int(guess)
    num_of_guesses += 1
    total_guesses -= 1
    if total_guesses == 0 and guess != secret_number:
        print("You ran out of guesses!!")
        break
    if guess == secret_number:
        print(
            f"You've Won!! It took {num_of_guesses} guess{'es' if num_of_guesses > 1 else ''}!"
        )
        break
    else:
        print("Wrong! Try Again!")
        continue
