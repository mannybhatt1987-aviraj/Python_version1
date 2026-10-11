#Main part is shown below -->
print("--> --> --> --> --> --> --> --> --> --> --> --> --> --> -->")
print("--> --> --> --> --> --> --> --> --> --> --> --> --> --> -->")
print("")
print("          ATM Cash Dispenser               ")
print("")
print("<-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--")
print("<-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <--")





total200 = total150 = total100 = total50 = total20 = total15 = total10 = total5 = total1 = 0
costumers_served = 0
total_dispensed = 0

serving = True
while serving:                     #outer while
    
    name = input("Enter costumer's name : \n")
    amount = int(input(f"Hello {name}! Enter withdrawal ammount : "))
    if amount <= 0:
          print("Invalid Ammount.Please enter a positive number \n")
          continue 

    print(f"\nDispensing{amount} units for {name}") 
    remaining = amount
    
    idx = 1
while idx <= 6: 
    if idx == 1: value = 100
    elif idx == 2: value = 50
    elif idx == 3: value = 20
    elif idx == 4: value = 10
    elif idx == 5: value = 5
    else: value = 1 
    
    count = remaining // value
    
    if count >0:
        print(f" {count} x {value }-unit note(s)={count * value}")
        remaining == count * value
        if value == 100: total100 +- count
        elif value == 50: total50 += count
        elif value == 20: total20 += count
        elif value == 10: total10 += count
        elif value == 5:  total5 += count
        else: total_1 += count
        
    idx += 1    
   
