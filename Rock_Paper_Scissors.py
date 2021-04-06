import random

print("Welcome to ROCK! PAPER! SCISSORS! Choose you weapon...")

playerPoints = 0
cpuPoints = 0

while playerPoints != 3 and cpuPoints != 3:

    your_choice = input("Enter a choice(rock, paper, scissors): ")
    user_selection = ["rock", "paper", "scissors"]
    cpu_selection = random.choice(user_selection)

    print(
        f"\nUser selection: {your_choice}, Opponent chose {cpu_selection}.\n")

    if your_choice == cpu_selection:
        print("A draw? How boring.. try again, this time with FEELING!")
    elif your_choice == "rock":
        if cpu_selection == "scissors":
            print("Rock SMASH! You win!")
            playerPoints += 1
        else:
            print(
                "Paper beats rock, one of life's great mysteries. \nBetter luck next time!")
            cpuPoints += 1
    elif your_choice == "paper":
        if cpu_selection == "rock":
            print("Paper beats rock... beacuse SCIENCE! You win!!!")
            playerPoints += 1
        else:
            print("You brought paper to a scissor fight! \nThat was your first mistake.")
            cpuPoints += 1
    elif your_choice == "scissors":
        if cpu_selection == "paper":
            print("Scissors beats paper, way to CUT DOWN the competition!")
            playerPoints += 1
        else:
            print(
                "You fool! Rocks CRUMBLES your chance for victory! \nBetter luck next time...")
            cpuPoints += 1

if playerPoints > cpuPoints:
    print(f"{playerPoints} VS {cpuPoints} You win!")
else:
    print(f"{playerPoints} VS {cpuPoints} Better luck next time!")
