import random

RockPaperScissorsList = ["rock", "paper", "scissors"]
YourScore = 0
ComputersScore = 0

while True:
    YourChoice = input("Choose rock, paper, or scissors. If you wish to quit, type q, and if you want to check the scores, type i: ").lower()

    if YourChoice == "q":
        print(f"The final score is: YOU: {YourScore} vs COMPUTER: {ComputersScore}")
        if YourScore > ComputersScore:
            print("Congratz! You win!")
            break
        else:
            print("Better luck next time!")
            break
        
    if YourChoice == "i":
        print(f"The current score: YOU {YourScore} vs COMPUTER {ComputersScore}")
        if YourScore > ComputersScore:
            print("Congratz! You're in the lead!")
        elif YourScore < ComputersScore:
            print("Aww. Seems like you're losing.")
        else:
            print("You have an equal score currently!")
  
        
    
    if YourChoice not in RockPaperScissorsList:
        continue
    
    ComputersChoice = random.choice(RockPaperScissorsList)
    
    print(f"Your choice: {YourChoice}, computers' choice: {ComputersChoice}")
    
    #scenarios
    
    if YourChoice == ComputersChoice:
        print("...continuing...")
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
            
    print(f"YOU: {YourScore} vs COMPUTER: {ComputersScore}")
        


