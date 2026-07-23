import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
round_number = 1

print("🎮 ROCK, PAPER, SCISSORS")
print("Enter 'quit' whenever you want to stop.\n")

while True:
    print(f"--- Round {round_number} ---")
    player = input("Choose rock, paper, or scissors: ").strip().lower()

    if player == "quit":
        break

    if player not in choices:
        print("❌ Invalid choice. Try again.\n")
        continue

    computer = random.choice(choices)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("🤝 It's a draw!")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "scissors" and computer == "paper")
        or (player == "paper" and computer == "rock")
    ):
        print("🎉 You win this round!")
        player_score += 1

    else:
        print("🤖 Computer wins this round!")
        computer_score += 1

    print(f"Score — You: {player_score} | Computer: {computer_score}\n")
    round_number += 1

print("\n🏁 FINAL SCORE")
print(f"You: {player_score}")
print(f"Computer: {computer_score}")

if player_score > computer_score:
    print("🏆 You won the game!")
elif computer_score > player_score:
    print("🤖 The computer won the game!")
else:
    print("🤝 The game ended in a draw!")

print("Thanks for playing!")
