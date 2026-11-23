"""
Number Guessing Game
--------------------
The computer picks a secret number and the player tries to guess it.
After each guess, the game says "too high" or "too low".

Concepts practiced: random module, while loops, counters, input validation
"""

import random


def play_round(low=1, high=100):
    """Play one round. Returns how many guesses it took."""
    secret = random.randint(low, high)
    guesses = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")

    while True:
        text = input("Your guess: ")
        if not text.isdigit():
            print("  Please type a whole number.")
            continue

        guess = int(text)
        guesses += 1

        if guess < secret:
            print("  Too low!")
        elif guess > secret:
            print("  Too high!")
        else:
            print(f"  You got it! The number was {secret}.")
            return guesses


def main():
    print("=== Number Guessing Game ===")
    best = None  # fewest guesses so far

    while True:
        guesses = play_round()
        print(f"It took you {guesses} guesses.")

        if best is None or guesses < best:
            best = guesses
            print("New best score!")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print(f"Thanks for playing! Your best score was {best} guesses.")
            break


if __name__ == "__main__":
    main()
    # Keeps the window open when you double-click the file on Windows
    input("\nPress Enter to exit...")
