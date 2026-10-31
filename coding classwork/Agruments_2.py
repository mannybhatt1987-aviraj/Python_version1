#Introduction to Doc String

def Factorial_number(a):
    '''This is the function to find Factorial_number'''
    if a == 0 or a == 1:
        return 1
    else :
        return a * Factorial_number(a-1)
    
print(Factorial_number(5))
print(Factorial_number.__doc__)


#The end of the 2nd activity

