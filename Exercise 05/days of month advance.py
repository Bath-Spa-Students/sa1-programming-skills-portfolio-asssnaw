#The following code is the dictionary mapping of the number of the month and number of the days each month contains.
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

#The following code asks the user to enter the number of the month they want to get the detail of.
try:
    month_number = int(input("Enter the month number (1-12): "))
    
    #This code helps to check if the number entered by the user is valid or invalid.
    if 1 <= month_number <= 12:
        #This code checks if the month number entered is the number of the month febuary (i.e 2)
        if month_number == 2:
           #This code asks the user to input the year number if the month number entered by user is 2
            year = int(input("Enter the year: "))
            #This code asks the user if in the above entered year was a leap year or not 
            leap_year = input(f"Is the year {year} a leap year? (yes/no): ").strip().lower()
            
            #If the user chooses Yes for the leap year 
            if leap_year == "yes":
                days[2] = 29  #Then the output will be given as 29 days in case of leap year
            #If the user chooses No for the leap year 
            else:
                days[2] = 28  #Then the output will be given as 28 days in case of Non-leap year
            
            # The bellow code will be used to print the number of days in case febuary month is chosen
            print(f"The month {month_number} (February) in {year} contains {days[month_number]} days.")
        else:
            # The bellow code will be used to print the number of days in case of other months except febuary 
            print(f"The month {month_number} contains {days[month_number]} days.")
    else: #The following statement will be printed and the user will be asked to reenter in case of invalid number
        print("The month number entered is invalid!!, Please enter a number between 1-12:") 
except ValueError: #The following will be printed in case the user does not enter the input in integer value and will be asked to reenter
    print("The input entered is ivalid!, Please enter a valid integer as the month number:")
