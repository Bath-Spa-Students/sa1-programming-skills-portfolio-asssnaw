#Following is the correct password that the user needs to enter to get access.
correct_pass = "12345"

#Here we will use the WHILE LOOP to repeadtly as the user the password until the correct passwored is entered.
while True:
   #The following statement is printed to ask the pasword to the user.
    enter_pass = input("Enter the password: ")
    
    #The following code is used to check if the password entered is the correct password or not.
    if enter_pass == correct_pass:
        #If the password entered matches with the correct password the following statement will be printed.
        print(" CONGRATS THE ACCESS IS GRANTED! The Password is correct!") 
        break  #Break is used to exsit the loop here the loop will end once thw user types the correct password.

    #Incase the password entered does not matches with the correct answer the loop will continue asking the user to renter the password.
    else: 
        print("The password entered is incorrect! Please try again.") 
