print("==============================shopping discount calculator======================")

valid = False
var_bill = float(input("ENter bill ammount "))
people = int(input("Enter the number of people "))
discount_ammount = 0 
while not valid:
    try:
        discount_ammount = var_bill * discount_ammount / 100
        final_bill = var_bill-discount_ammount
        each_person_who_has_to_pay = final_bill / people
    except ValueError:
        print("Type a number ")
    except ZeroDivisionError:
        print("Can't divide by 0")
    else:
        print(f"Each person has to pay {each_person_who_has_to_pay}")
        valid = True
    finally:
        print("Always executed")               