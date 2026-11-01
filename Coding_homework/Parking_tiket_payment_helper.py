#Important part : Decorate the heading

print("========parking ticket payment helper========")

#Part 1 : Create the change function

def change_calculator(paid,price):
    total = paid - price
    return total

#Part 2 : Set up the ticket price 

ticket_price = 40


print("Notes ₹10,₹20,₹50,₹100,₹200 and ₹500 are inserted in the ticket.")

#Part 3 : Create starting counters 

total_inserted_notes = 0
notes_inserted = 0

#Part 4 : Start the while loop 

while True:
    
    ruppee_notes = int(input("Please enter ₹10,₹20,₹50,₹100,₹200 and ₹500 : "))
    
#Part 5 : Skip invalid notes with the CONTINUE 

    if ruppee_notes != 10 and ruppee_notes != 20 and ruppee_notes != 50 and ruppee_notes != 100 and ruppee_notes != 200 and ruppee_notes != 500 : 
        print("Invalid notes. Please enter again as ruppee is our respective currency.")
        continue
    
#Part 6 : Add valid notes 

    notes_inserted += 1
    
    
#Part 7 : Stop the loop with BREAK 
   
    change_due = change_calculator(total_inserted_notes,ticket_price)
   
   
    if total_inserted_notes >= ticket_price:
     print("Enough rupee notes.")
     break
    
    
#Part 8 : Use PASS when no change is needed 

    
if change_due == 0:
     pass
 
 #Part 9 : Print the final Summary
 
print("\n===== PAYMENT SUMMARY =====")
print("Ticket Price:", ticket_price)
print("Coins Inserted:", notes_inserted)
print("Total Paid:", total_inserted_notes)
print("Change Given:", change_due)
print("===========================")
print("Parking ticket payment complete!")
   
 