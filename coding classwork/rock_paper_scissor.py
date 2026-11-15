#Rock paper scissor

import random
while True:
    user = input("What is your guess ? rock paper or scissor?  ")
    DELL_laptop = random.choice (["rock","paper","scissors"])
    
    print(f"Your guess is {user}")
    print(f"DELL laptop's guess is {DELL_laptop}")
    
    continue_process = input("Do you want to continue this game? (Yes/no)?")
    if user == DELL_laptop:
            print("A tie !") 
    elif user == "rock" and DELL_laptop == "scissor":
        print("You win!")
    elif user ==  "scissor" and DELL_laptop == "paper":
        print("You win")
    elif user == "paper" and DELL_laptop == "rock":
        print("You win!")     
    else : 
        print("You lost")
                     
            
              
    if continue_process == "no":
        print("OKay")
        break
    else : 
        print("Okay we will continue  ")
        
    