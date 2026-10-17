print("floyds traingle")

n = int(input("Enter the number of rows : "))

number = 1

for row in range (n):
    for n in range (row+1):
        print(number, end="")
        number = number+1
    print()    