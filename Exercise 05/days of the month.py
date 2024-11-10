#The following code is the dictionary mapping of the number of the month and number of the days each month contains
days = {
    1: 31,   # January contains 31 days
    2: 28,   # February contains 28 days (non-leap year)
    3: 31,   # March contains 31 days
    4: 30,   # April contains 30 days
    5: 31,   # May contains 31 days
    6: 30,   # June contains 30 days
    7: 31,   # July contains 31 days
    8: 31,   # August contains 31 days
    9: 30,   # September contains 30 days
    10: 31,  # October contains 31 days
    11: 30,  # November contains 30 days
    12: 31   # December contains 31 days
}

#The following code asks the user to enter the number of the month they want to get the detail of 
try:
    month_number = int(input("Enter the number of the month (i.e. 1-12): "))

#This code helps to check if the number entered by the user is valid or invalid 
    if 1 <= month_number <= 12:
       #If the input entered is valid then print the bellow statement
        print(f"The month {month_number} contains {days[month_number]} days.") 
    #If the input entered is invalid then the bellow statement will be printed asking the user to renter the valid value
    else:
        print("The month number entered is invalid!!, Please enter a number between 1-12: ")
    #If the input entered is not in integer value, the following statement will be printed asking the user to print an integer value.
except ValueError:
    print("The input entered is ivalid!, Please enter a valid integer as the month number: ")
