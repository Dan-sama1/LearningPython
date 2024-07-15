import random
choices = ['rock', 'paper', 'scissors']
result = {
    'rock': {'rock': 'Tie!', 'paper': 'You Lose!', 'scissors': 'You Win!'},
    'paper': {'paper': 'Tie!', 'scissors': 'You Lose!', 'rock': 'You Win!'},
    'scissors': {'scissors': 'Tie!', 'rock': 'You Lose!', 'paper': 'You Win!'}
}
looper = True
while looper:
    computer = random.choice(choices)
    print("Rock, paper or scissors?", end="\n")
    player = input(">> ").lower()

    if player not in choices:
        print("Invalid choice, please try again...")
        input("Press any key to continue...")
        continue

    print(f"Computer: {computer}")
    print(f"Player: {player}")
    print(f"{result[player][computer]}")

    while True:
        chooser = input("Play again [Y/N]? ").upper()
        if chooser == 'Y':
            break
        elif chooser == 'N':
            looper = False
            input("Press any key to continue...")
            break
        else:
            print("Invalid! Please try again...")

print("THANK YOU FOR PLAYING!! :)")
