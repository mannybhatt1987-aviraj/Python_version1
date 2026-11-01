print("====Vending machine====")

def change_calculator(amount,price):
    change = amount - price
    return change

price_of_snack = 11
print(f"price of snacks are : {price_of_snack}")
print("The coin that are accepted in the machine are $1,$2,$10, and $5.")

coins = 0

while True:
    
    total_dollar_coins = int(input("Enter coins $1,$2,$5 and $10 : "))
 
    
    if total_dollar_coins != 1 and total_dollar_coins != 2 or total_dollar_coins != 5 or total_dollar_coins !=10:
        print("Invalid Dollar coins.")
        continue 
    
    coins += total_dollar_coins
    print(f"Coins that are inserted so far are : {coins}")
    if coins >= price_of_snack:
        print("Enough Dollar coins!")
        break
    
    
    
    change = change_calculator(coins,price_of_snack)
    
    if change == 0:
        pass
    else : 
        print(f"Change due is : {change}")
        