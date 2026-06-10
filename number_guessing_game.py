import random


def display_welcome():
    print("=" * 50)
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME 🎮")
    print("=" * 50)
    print("I have selected a random number between 1 and 100.")
    print("Can you guess it?\n")


def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def play_game():
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < random_number:
            print("📉 Too low! Try a higher number.\n")
        elif guess > random_number:
            print("📈 Too high! Try a lower number.\n")
        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the correct number: {random_number}")
            print(f"Number of attempts: {attempts}")

            if attempts <= 5:
                print("Excellent guessing skills! 🌟")
            elif attempts <= 10:
                print("Good job! 👍")
            else:
                print("You got it eventually! 😊")

            break


def play_again():
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").lower()

        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    display_welcome()

    while True:
        play_game()

        if not play_again():
            print("\nThank you for playing the Number Guessing Game!")
            print("Goodbye! 👋")
            break


if __name__ == "__main__":
    main()