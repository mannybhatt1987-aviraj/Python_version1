print("===========Addition Game===========")


calculating = True
name = input("Enter your name : ")
print("")
print(f"Hello {name}!")
print("")
age = int(input(f"Enter your age {name} : "))
print("")

addition = 0

if age <= 4:
    print("You can't Do it .")
    print("") 
    
else :
 print("You can do this.")
 print("")
 print("Can you solve this addition ?")
 print("")
 print("    TH H T O   ")
 print("")
 print("     1 2 3 4   ")
 print("   + 5 7 6 8   ")
 
 answer = int(input("Answer : "))

if answer < 7002:
    print("It is lower than expected .")
    print("")
elif answer > 7002:
    print("It is higher than expected .")
    print("")
else :      
    if answer == 7002:
     print("Correct Answer!")
     print("")
     

                            
    
