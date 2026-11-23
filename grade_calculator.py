"""
Grade Calculator
----------------
Asks for a student's scores, calculates the average,
and turns it into a letter grade.

Concepts practiced: input, loops, lists, functions, if/elif/else
"""


def get_letter_grade(average):
    """Turn a number average into a letter grade."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_score(prompt):
    """Keep asking until the user types a valid score between 0 and 100."""
    while True:
        text = input(prompt)
        try:
            score = float(text)
        except ValueError:
            print("  Please type a number.")
            continue
        if 0 <= score <= 100:
            return score
        print("  Scores must be between 0 and 100.")


def main():
    print("=== Grade Calculator ===")
    name = input("Student name: ")

    # Ask how many scores to enter (must be at least 1)
    while True:
        try:
            count = int(input("How many scores? "))
            if count > 0:
                break
            print("  Enter at least 1.")
        except ValueError:
            print("  Please type a whole number.")

    scores = []
    for i in range(1, count + 1):
        scores.append(get_score(f"  Score {i}: "))

    average = sum(scores) / len(scores)
    letter = get_letter_grade(average)

    print()
    print(f"Student:  {name}")
    print(f"Scores:   {scores}")
    print(f"Highest:  {max(scores)}")
    print(f"Lowest:   {min(scores)}")
    print(f"Average:  {average:.2f}")
    print(f"Grade:    {letter}")


if __name__ == "__main__":
    main()
    # Keeps the window open when you double-click the file on Windows
    input("\nPress Enter to exit...")
