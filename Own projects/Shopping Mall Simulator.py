print("==================================================================")
print("==================================================================")
print("")
print("                Shopping Mall Simulator                           ")
print("")
print("==================================================================")
print("==================================================================")
print("")

high_price_items = 0
medium_price_items = 0
low_price_items = 0
customers_served = 0
total_dollars_spent = 0
shopping = True

Name = input("Enter customer name : ")
print(f"Hello {Name}!")
print("There are 8 rooms")
print("1. King Shoes (For shopping of shoes)")
print("2. Happy Valley (For shopping of fruits and vegetables)")
print("3. Little Detectives (Play Zone(Also includes a shopping area))")
print("4. Pet Care (A vetenary clinic)")
print("5. Cats cats cats (Shopping for pet cats)")
print("6. Salmon meat (A salmon meat shop)")
print("7. Doggy Dog Man (Shopping For Dog Man comics)")
print("8. The Supa Buddies Club (The bonus of Supa Buddies(Dog Man))")
rooms = int(input("Which room you want to go?"))
print("")

if rooms == 1:        
    print("You picked King Shoes")
    print("You will do shoes shopping")
    print(f"Have a nice day {Name}!")
elif rooms == 2:
    print("You picked Happy Vally Market")
    print("You will do shopping of fruits & Vegetables")
    print(f"Have a nice day {Name}!")
elif rooms == 3:
    print("You picked Little detectives Play zone")
    print("You will do shopping and your children will play")
    print(f"Have a nice day {Name}!")
elif rooms == 4:
    print("You picked Pet care Vetenary clinic")
    print("Your pet will be healed")
    print(f"Have a nice day {Name}!")
elif rooms == 5:
    print("You picked Cats cats Cats ")
    print("You will do shopping of pet cats")
    print(f"Have a nice day {Name}!")                 
elif rooms == 6:
    print("You picked Salmon Meat shop")
    print("You will do shopping of Salmon Meat")
    print(f"Have a nice day eating Salmon Meat {Name}!")
elif rooms == 7:
    print("You picked Doggy Dog Man Dog Man Comic Shop")
    print("You will do shopping Of Dog Man Comics")
    print(f"Have a nice day {Name}!")
elif rooms == 8:
    print("You picked Supa Buddies Club")
    print("You will do shopping of Supa Buddies Mega collection(dog man)")
    print(f"Have a nice day {Name}!")
else:
    print("Invalid Input")    
                         