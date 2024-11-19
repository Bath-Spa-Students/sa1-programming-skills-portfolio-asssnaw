#The bellow code determines if a number is even or odd .
def even_or_odd(number):
    if number % 2 == 0: # If the number is even the following statement is printed .
        return f"The number {number} is an even number."
    else: # If the code is odd the following statement is printed .
        return f"The number {number} is an odd number."

# The following is the code for the main function.
def main():
    try:
        # The following code shows the user that the program is running.
        print(" The Program has started. Waiting for the user to enter an input...")
        
        # The following code asks the user to enter a number.
        number = int(input("Please enter a number: "))
        
        # The following code calls the funtion to check if number is even or odd and then store the reult obtained.
        result = even_or_odd(number)
        
        # The following code assures the user that the function is taking place .
        print("The Function was executed. Now preparing to display the result...")
        
        # The following function prints the final result.
        print(result)
    
    except ValueError: #This code runs when the number entered by the user is not an integer.
        print("Input entered is invalid! Please enter a valid integer number.")

# The following code calls the main funtion to run the program. 
if __name__ == "__main__":
    # The following code indicates to thr user that the script is being executed directly.
    print("The script is being executed directly.")
    main()
