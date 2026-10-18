print("=====Test Project =====")

secret_number = 40

attempt = 5
i = 0
name = input("Enter your name : ")
print(f"Hello {name}")



while i  < attempt:
    
    
   guess = int(input("Enter your guess from 1 to 50 : "))
   
   if guess < 1 or guess > 50 : 
          print("Invalid")  
 
   elif guess == secret_number:
       print("You  win")
   elif guess < secret_number:
       print("Not correct.Try again.")
   elif guess > secret_number:
       print("Not correct.Try again.")
   
       
       i = i + 1         
       print("Attempts Left :", attempt - i )
       
   if i == attempt and guess != secret_number :
         
           print("Game Over !")
           