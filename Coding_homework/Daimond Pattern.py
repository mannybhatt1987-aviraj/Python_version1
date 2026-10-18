#Main part :  decorate the heading
print("=============================")
print("=============================")
print("Diamond Pattern")
print("=============================")
print("=============================")

#Part 1 : Create the star pyramid section

star_pyramid_section = int(input("Enter The number of rows : "))

#Part 2 : Biuld Row and columns with nested loops

for row in range (4):
    for plus in range (row+1):
    
#Part 3 : Keep output on one line 

      print("+" ,end="")
      print()
    
 #Part 4 : Create Floyds Triangle
 
y = int(input("Enter No. of rows : "))

no = 1

for row in range (y):
    for y in range (row+1):
        print(no ,end="")
        no = no+1
        print() 
        
 #Part 5 : Count up across every row
 
 
 