print("-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
print("")
print ("                   Grocery Billing Queue                                               ")
print("")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
print("")

low_price_items = 0
medium_price_items = 0
high_price_items = 0

customers_served = 0
total_sales = 0

billing = True

total_sales += 500

while billing: 

    customer_name = input("Enter Customer Name: ")
    print(f"Hello {customer_name}!")
    print("")  
    item_count = int(input(f"How many items are you buying,{customer_name}?\n"))
    
    if item_count <= 0:
      print("Please enter a valid number of items.")
      continue
  

item_count <= 0


customer_total = 0
item_number = 1

while item_number <= item_count:
    item_name = input("Enter item name: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    if price == 67 and quantity == 1:   
        print(f"The price of your item is {price} and quantity is {quantity}")   #outer if
check = input("Do you have this much VS Code Dollars? (Yes/no)?").lower() 
if check == "yes":     #inner if 
    
    print("Okay,you could buy this item.\n")
elif check == "no":
    
    print("You could not buy this if you don't have this much VS Code Dollars.")
else:
    
    print("Invalid Input")         
    
while item_number <= item_count:
    
    if price <= 0 or quantity <= 0:
       print("Price and quantity must be positive.")
       print(f"Your price was {price} and quantity was {quantity}")
    continue

item_total = price * quantity

print(f"{item_name}: {quantity} x {price} = {item_total}")

customer_total += item_total

if price < 50:
    low_price_items += quantity
elif price <= 100:
    medium_price_items += quantity
else:
    high_price_items += quantity

item_number += 1
if price <= 0 or quantity <= 0:   
    item_total = price * quantity
        
    print(f" ")