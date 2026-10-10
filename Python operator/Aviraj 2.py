print("=========================================")
print("=========================================")
print("")
print("        Car Chooser            ")
print("")
print("=========================================")
print("=========================================")
print("")

Car = int(input("Enter 1 or 2"))
print("1 - sports car")
print("2 - 7 seater car")
print("")

if Car ==1:    #outer if
    print("You picked : sports car")
   car = int(input("Enter 2 or 3"))
   print("2 - Lamborghini Huracun")
   print("3 - Mercedes AMG")
if car == 2:  #inner if
    print("You picked : Lamborghini Huracun")
    print("Short form : Lambo")
    print("Top speed : 325 km/h (202 mph)")
    print("Very fast and could beat Ferrari")
elif car == 3:
    print("You picked : Mercedes AMG")
    print("Short form : AMG")
    print("Top speed : 352 km/h (219 mph)")
    print("very fast and can beat Lamborghini Huracun")
else :
    print("Invalid input")    
     
        
    