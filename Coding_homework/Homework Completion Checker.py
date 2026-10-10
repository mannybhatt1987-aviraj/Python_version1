#Main Part : Give The Heading And Decorate It
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("")
print("    Homework Completion Checker  ")
print("")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=")

 
# PART 1: Set today's total number of homework tasks
total_homework = 4
original_count = total_homework
print(f"You have {original_count} homework tasks to finish today!\n")
 
# PART 2: Keep a counter for completed homework and the current task number
completed_count = 0
task_num = 1
 
# PART 3: Repeat while there are still homework tasks left
while task_num <= total_homework:
 
    # PART 4: Work out the current homework task from its number
    if task_num == 1:
        next_task = "Math worksheet"
    elif task_num == 2:
        next_task = "Science reading"
    elif task_num == 3:
        next_task = "English writing"
    else:
        next_task = "Coding practice"
 
    finishing_question = input(f"Have you finished: {next_task}? (yes/no): ")
 
    # PART 5: Only move on once the task is marked done
    if finishing_question == "yes":
        completed_count += 1
        task_num += 1
        print("Great job! Homework completed!")
    else:
        print("No problem.Finish it ")
 
    # PART 6: Print how many homework tasks remain
    print("Homework tasks remaining:", total_homework - completed_count)
    print()
 
# PART 7: This only prints once every homework task is marked done
print("===== ALL HOMEWORK COMPLETE! =====")
print("Great work finishing your homework today!\n")
 
# PART 8: A safe look at what an infinite loop would look like
print("Now a look at infinite loop...")
value = 0
safety_counter = 0
 
while value <= 0:
    print("This would run forever!")
    safety_counter += 1
 
    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break
 
# PART 9: Print the final homework checklist summary
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("")
print("    HOMEWORK DONE!!")
print("")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

