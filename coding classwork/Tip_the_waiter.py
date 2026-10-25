print("===Tip the waiter===")

#Tip the waiter
#Define a function to calculate the tip on bill

def calculated(bill,tip_perc):  #2 Arguments & 1 def function
    total = bill * (1 + 0.01*tip_perc ) #20 * 0.01  = 0.20 + 1=1.20 150*1.20 = 180
    total = round(total,2) #round -up the total amt/bill
    print(f"Please pay ${total}")
    
   #specify only bill amt
   #Default value of tip percentage is used
   
calculated(150,20)  