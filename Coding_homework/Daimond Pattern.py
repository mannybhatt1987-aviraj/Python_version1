print("=============Daimond Pattern=============")
print("")

name = input("Enter your name : ")
print("")
print(f"Hello {name}!")
print("")
rows = int(input(f"Enter the number of your rows {name} : "))
print("")
no = 1

row = int(input("Enter number of rows (down) "))

for i in range (rows):
     for space in range(rows-i-1):
         print("" ,end="")
         for j in range (i+1):
             print(no ,end="")
             
             no = no+1
        
     print()    
     
     
if row%2 ==0:
   half= row//2
else:
    half= row//2 +1

space=half-1
number=1
for i in range(1,half+1):
   for j in range(1,space+1):
       print(end="* ")
   space=space-1
   num=1
   for k in range(2*i-1):
       print(num,end=" ")
       number=number+1

   print()

space=1
for i in range(1,half):
   for j in range(1,space+1):
      print(end="# ")
   space=space+1
   num=1
   for k in range(1,2*(half-i)):
      print(num,end=" ")
      num=num+1
   print()    

