# ROCK PAPER SCISSORS GAME
import random
# SCORE VARIABLES
user_score = 0
computer_score = 0
# CHOICES
choices = ["rock", "paper", "scissors"]
# GAME LOOP
while True:
    print("\n===== ROCK PAPER SCISSORS =====")
    # USER INPUT
    user = input("Enter rock, paper or scissors: ").lower()
    # VALIDATION
    if user not in choices:
        print("Invalid choice. Try again.")
        continue
    # COMPUTER CHOICE
    computer = random.choice(choices)
    print("Computer chose:", computer)
    # GAME LOGIC
    if user == computer:
        print("It's a Tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1
    # DISPLAY SCORES
    print("\nScore Board")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
    # PLAY AGAIN
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break