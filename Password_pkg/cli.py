"""Command Line Interface for Password Strength Checker."""

import getpass
from .checker import analyze_password


def print_line():
    print("=" * 60)


def show_report(password):

    report = analyze_password(password)

    print_line()
    print("          PASSWORD STRENGTH REPORT")
    print_line()

    if report.length == 0:
        print("Please enter a password.")
        return

    print("\nGENERAL INFORMATION")

    print("Password Strength :", report.strength)
    print("Total Score       :", report.score, "/", report.maximum_score)
    print("Score Percentage  :", report.score_percentage, "%")
    print("Password Length   :", report.length)
    print("Character Variety :", report.character_variety, "/4")

    print("\nCHARACTER CHECKS")

    print("Lowercase Letters :", "Yes" if report.has_lowercase else "No")
    print("Uppercase Letters :", "Yes" if report.has_uppercase else "No")
    print("Numbers           :", "Yes" if report.has_digit else "No")
    print("Symbols           :", "Yes" if report.has_symbol else "No")

    print("\nPATTERN CHECKS")

    print("At least 8 chars  :", "Yes" if report.has_minimum_length else "No")
    print("At least 12 chars :", "Yes" if report.has_recommended_length else "No")
    print("At least 16 chars :", "Yes" if report.has_long_length else "No")
    print("Common Password   :", "Yes" if report.is_common else "No")
    print("Repeated Character:", "Yes" if report.has_repeated_run else "No")
    print("Simple Sequence   :", "Yes" if report.has_sequence else "No")

    print("\nESTIMATED ENTROPY")

    print(report.estimated_entropy_bits, "bits")

    print("\nSUGGESTIONS")

    for number, suggestion in enumerate(report.feedback, 1):
        print(f"{number}. {suggestion}")

    print("\nPRIVACY INFORMATION")
    print("Your password is analyzed locally.")
    print("It is not saved to a file or sent to a server.")
    print("The entropy value is only a rough estimate.")

    print_line()


def ask_to_continue():

    while True:

        choice = input(
            "\nAnalyze another password? (y/n): "
        ).strip().lower()

        if choice in ("y", "yes"):
            print("\nStarting a new password analysis...\n")
            return True

        elif choice in ("n", "no"):
            print("\nThank you for using Password Strength Checker!")
            return False

        else:
            print("Invalid choice! Please enter only y or n.")


def main():

    print_line()
    print("       ADVANCED PASSWORD STRENGTH CHECKER")
    print_line()

    print("Welcome to the Password Strength Checker!")
    print("Enter a sample password for demonstration.")
    print("Your input will be hidden while typing.")

    while True:

        print("\nENTER PASSWORD")

        password = getpass.getpass(
            "Enter a password to analyze: "
        )

        show_report(password)

        if not ask_to_continue():
            break


if __name__ == "__main__":
    main()