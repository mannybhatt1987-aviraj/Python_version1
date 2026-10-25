#Define function to calculate cub 
def cube(number):
    return number * number * number
#another function whether the number is divisible by 3
def divisible_by_three(number): #% --> remainder
    if number % 3 == 0:
        return cube(number) #call cube function
    else :
        return False
    #Display result
print(divisible_by_three(9)) #Divisible by 3
print(divisible_by_three(4)) #Not Divisible by 3
