print("==========================================")
print("Welcome to the  Ride Builder factory!")
print("===========================================")
print("")

print("Pick your vehicle")
print("1-car")
print("2-bike")
print("")

choice = int(input("Enter 1 or 2"))
print("")

if choice == 1:  #outer if
 
     print("Pick your car type")
     print("1-BMW 6 series")
     print("2-Hyundai verna")
     
     car_type = int(input("Enter 1 or 2"))
     
     if car_type == 1: #inner if
         
         print("you picked : BMW 6 series")
         print("Top speed : 250 km/h (155 mph)")
         print("good for normal & racing purposes")
     else:
         print("you picked : Hyundai verna ") 
         print("Top speed : 210 km/h") 
         print("good for driving purposes")
         print("")
         
           
elif choice == 2: #outer if
    
      print("Pick your bike type")
      print("1- Hayabusa")
      print("2- Yamaha")
      
      bike_type = int(input("Press 1 or 2"))
      
      if bike_type == 1: #inner if 
          print("You picked : Hayabusa")
          print("Top speed : 299 km/h (186 mph)")
          print("Good for racing")
          print("")
      else: 
          
           print("You picked : Yamaha ")
           print("Top speed : 250km/h")
           print("Good for racing")   
else:
      print("Invalid input")        