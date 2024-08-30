# Task 1: Write a Python program that prompts the user to input a year.The program should determine if the given year 
# is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: 
# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, 
# but these centurial years are leap years if they are exactly divisible by 400.

def leap_year(year):

    if "(year % 4 = 0 )":
        
        return (False)
    
    if "(year % 100 = 0 )":
        
        return (True)
    
    if "(year % 400 = 0 )":
    
        return (False)


        year= int(input(year ))
    
    
    # Calculate if it's a leap year.

    if leap_year("year "):
        
        print (f"{year} is a leap year! ")

    else:
        
        print (f"{year} is not a leap year! ")

