import random

RockPaperScissorsList = ["rock", "paper", "scissors"]
YourScore = 0
ComputersScore = 0

while True:
    YourChoice = input("Choose rock, paper, or scissors. If you want to quit, type q: ").lower()

    if YourChoice == "q":
        print(f"The final score is: YOU {YourScore} vs COMPUTER {ComputersScore}")
        if YourScore > ComputersScore:
            print("Congratz! You win!")
            break
        else:
            print("Better luck next time!")
            break
    
    if YourChoice not in RockPaperScissorsList:
        continue
    
    ComputersChoice = random.choice(RockPaperScissorsList)
    
    print(f"Your choice was {YourChoice}, computers' choice was {ComputersChoice}")
    
    #scenarios
    
    if YourChoice == ComputersChoice:
        continue
    
    elif YourChoice == "rock":
        if ComputersChoice == "scissors":
            YourScore += 1
        elif ComputersChoice == "paper":
            ComputersScore += 1
            
    elif YourChoice == "paper":
        if ComputersChoice == "rock":
            YourScore += 1
        elif ComputersChoice == "scissors":
            ComputersScore += 1
    
    elif YourChoice == "scissors":
        if ComputersChoice == "paper":
            YourScore += 1
        elif ComputersChoice == "rock":
            ComputersScore += 1
            
    print(f"Your current score is {YourScore} and computers' score is {ComputersScore}")
        


