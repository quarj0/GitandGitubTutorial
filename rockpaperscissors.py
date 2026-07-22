user1="rock"
user2="paper"
user3="scissors"

print(
    """
    ==============================
    WELCOME TO ROCK PAPER SCISSORS
    ==============================
    """
)
print("Player1")
print("Player2")
print("Player3")
print("Choose a player from [player1, Player2, Player3] to ")
choose_player = input()

if choose_player in ["player1, Player2, Player3"]:
    if choose_player == "player1":
        print("You chose player1")