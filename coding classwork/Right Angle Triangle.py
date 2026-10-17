print("Right angle triangle")

angle = int(input("Enter number of rows : "))

for row in range(angle):
    for stars in range(row+1):
        print("*" ,end="")
    print()    
        
    
         