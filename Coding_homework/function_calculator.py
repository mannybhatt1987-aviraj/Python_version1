def add(a,b):
 return a + b
def minus(a,b):
   return a - b
def multiply(a,b):
 return a * b 
def divide(a,b):
 return a / b
 
 
try:
   choice = int(input("Choose (1-4) : ")) 
   number1 = float(input("Enter number 1 : "))
   number2 = float(input("Enter number 2 : "))

   if choice == 1:
    result = add(number1,number2)
    print(f"result is {result}")
   elif choice == 2: 
    result = minus(number1,number2)
    print(f"result is {result}")
   elif choice == 3:
    result = multiply(number1,number2)
    print(f"result is {result}")
   elif choice == 4:
    result = divide(number1,number2)
    print(f"result is {result}")  
   else:
    print("Invalid choice!")
  
except ValueError:
 print("please enter  numbers ")
except ZeroDivisionError:
 print("No zero is not divided!")      








