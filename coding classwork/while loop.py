#checklist checker
print("------------------------------")
print("------------------------------")
print("")
print("       My chore ckecklist    ")
print("")
print("------------------------------")
print("------------------------------")

total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to complete")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    
    if chore_num == 1: Task = "Make your bed"
    elif chore_num == 2: Task = "Feed the pet"
    elif chore_num == 3: Task = "Clean the trash"
    else : Task = "Wash the dishes"
    
    answer = input("Have you finished : {task} ? (yes/no)").lower()
    
    if answer == "yes":
        completed_count += 1
        chore_num += 1
        
        print("Great job! Chore completed!")
        
    else:
        print("Ok,finish it. No problem")   
        
        print("------------------------------")
        print("------------------------------")
        print("")
        print("   All Chores Completed!  ")
        print("")
        print("------------------------------")
        print("------------------------------")  