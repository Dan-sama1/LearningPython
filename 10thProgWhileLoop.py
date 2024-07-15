life = 3
num = 7
guesser = 1
while life > 0:
    print(f"Life: {life}")
    guess = int(input(f"Guess {guesser}: "))
    if guess == num:
        print("you win!")
        break
    life = life - 1
    guesser = guesser + 1
else:
    print('you lose')
