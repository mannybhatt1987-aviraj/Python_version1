try:
    number_1 = int(input("Enter number 1 : "))
    number_2 = int(input("Enter number 2 : "))
    result = number_1/number_2
    print(f"result is {result}")
 
except ZeroDivisionError : 
     print("We cannot divide it with 0 ")    
    
except ValueError : 
    print("Please enter a number . ")
   
except : 
    print("Invalid.")
else : 
    print("no exeption.") 
finally :
    print("Always excetuted")       
        
        