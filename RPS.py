import random

RockPaperScissorsList = ["rock", "paper", "scissors"]
YourScore = 0
ComputersScore = 0

while True:
    YourChoice = input("Choose rock, paper, or scissors. If you want to quit, type q: ").lower()

    if YourChoice is "q":
        break
    
    if YourChoice in RockPaperScissorsList:
        continue
    
    ComputersChoice = random.choice(RockPaperScissorsList)
    
    #scenarios
    
    if YourChoice == ComputersChoice:
        continue
    
    if YourChoice is "rock":
        if ComputersChoice is "scissors":
            YourScore += 1
        if ComputersChoice is "paper":
            ComputersScore += 1
            
    if YourChoice is "paper":
        if ComputersChoice is "rock":
            YourScore += 1
        if ComputersChoice is "scissors":
            ComputersScore += 1
    
    if YourChoice is "scissors":
        if ComputersChoice is "paper":
            YourScore += 1
        if ComputersChoice is "rock":
            ComputersScore += 1
            
    print(f"Your current score is {YourScore} and computers' score is {ComputersScore}")
        


