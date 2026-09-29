

print("Welcome to the swimming pool!")
print("Please answer the following questions to determine if you can swim in the pool.")



Age = int(input("Enter your age: "))

beginner = input("Are you a beginner? (yes/no): ")

coaching = input("Do you need coaching? (yes/no): ")

checking_pool = input("Is the pool safe for you? (yes/no): ")

if Age >= 9 or beginner.lower() == "yes" and checking_pool.lower() == "no":
    print("You cannot swim in the pool.")

elif Age < 9 and beginner.lower() == "no" and checking_pool.lower() == "no":
    print("You cannot swim in the pool.")
    
elif Age >= 9 and beginner.lower() == "no" and checking_pool.lower() == "yes":
    print("You can swim in the pool.")    
    
else:       
    print("You cannot swim in the pool.") 
 