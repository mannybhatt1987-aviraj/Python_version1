print("==========Lemonade Stand==========")

def greet_a_custumer():
    print("Welcome to the lemonade stand!")
    print("Fresh Lemonade, made just for you!")
    
    
    
greet_a_custumer()

 
price = 40
cups_sold = int(input("Enter the number of sold cups : "))

def total_calculated(price,cups_sold):
    total = price * cups_sold
    return total

total_cost = total_calculated(price,cups_sold)
print(f"Total cost is : {total_cost}") 

ammount_paid = float(input("Enter the Ammount paid by the costumer : "))

def calculate_change(paid,total):
    change = paid - total
    return change

change = calculate_change(ammount_paid,total_cost)
print(f"change due is {change}")
