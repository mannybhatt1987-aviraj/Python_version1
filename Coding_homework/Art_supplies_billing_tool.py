def friendly_greeting():
    print("Welcome to Art supplies billing tool store! ")
    print("You could take any item you want! ")
    

friendly_greeting()  
   

item_count = float(input("Enter the number of items bought : "))   
price_per_item = int(input("Enter the price of items  : "))

def total_calculated(price,items):
     total = price*items
     return total
 


total_cost = total_calculated(price_per_item,item_count)

def calculate_change(paid,total):
    change = paid - total
    return change
    
    
    
def thank_you_message(items):
       if items >= 5:
           print("Thank you shopping for art items at the art store!") 
       elif items <= 5:
           print("That means you didn't like the art items.But no problem.")
       else : 
           return "Thanks for shopping!"
 
 
       
ending_message = thank_you_message(item_count)

print(f"price per item = {price_per_item}")
print(f"items that you bought = {item_count}")
print(ending_message)            