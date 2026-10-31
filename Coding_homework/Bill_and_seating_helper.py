#Bill and seating helper

#Part 1 : Create the bill function 

def bill(bill_amount,perc):
    total = bill_amount + (bill_amount * perc/400)
   
    print(f"You have to pay ₹{total}")
    
#Part 2 : Call the function with positional arguments

bill(450,60)     

#Part 3 : Create the recursive Seating function 

def seating_arrangement(guests):
    '''It calculates the seatig arrangement'''
    
#Part 4 : Add the base case 
    if guests == 0 or guests == 1 :
       return 1

#Part 5 : Add the recursive case 
    else : 
      return guests * seating_arrangement(guests - 1)

#Part 6 : Access the docstring 
print(seating_arrangement.__doc__)

#Part 7 : Display seating results

print("Seating arrangements for 1 guest:", seating_arrangement(1))
print("Seating arrangements for 2 guests:", seating_arrangement(2))
print("Seating arrangements for 3 guests:", seating_arrangement(3))
print("Seating arrangements for 5 guests:", seating_arrangement(5))

#Part 8 : Run and Explore!
print("The end")
#The end of homework 

