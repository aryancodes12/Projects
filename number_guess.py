import random

# Random number between 1 and 6
choices = random.randint(1, 6)
Chance = 3

print("\n\033[1;96m🎲 Welcome to Guess The Number!\033[0m")
print("\033[1;93mGuess a number between 1 to 6. You have 3 chances.\033[0m\n")

for i in range(Chance):
    print(f"\033[1;92mChances left: {Chance}\033[0m")
    user_input = input("\033[1;94mEnter your guess or type 'q' quit: \033[0m")

    if user_input.lower() == "q":
        print(f"\n\033[1;91mYou exited the game. The number was: {choices}\033[0m")
        print("\033[1;95mThank you for playing!\033[0m")
        break

    try:
        user_guess = int(user_input)
    except ValueError:
        print("\033[1;91mInvalid input! Please enter a number between 1 and 6.\033[0m\n")
        continue

    if user_guess < 1 or user_guess > 6:
        print("\033[1;91mNumber must be between 1 and 6.\033[0m\n")
        continue

    Chance -= 1

    if user_guess == choices:
        print("\n\033[1;92m🎉 Congrats! You guessed it right!\033[0m")
        break
    elif user_guess < choices:
        print("\033[1;93mHint: Go higher.\033[0m\n")
    elif user_guess > choices:
        print("\033[1;93mHint: Go lower.\033[0m\n")

else:
    print(f"\n\033[1;91m😢 You're out of chances. The number was: {choices}\033[0m")

print("\033[1;96mGame Over.\033[0m\n")
