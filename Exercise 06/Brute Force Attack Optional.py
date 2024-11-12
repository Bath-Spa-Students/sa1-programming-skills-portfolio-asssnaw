#Following is the correct password that the user needs to enter to get access.
correct_pass = "12345"

#The following shows the maximum number of attempts the user can use to type the password.
max_attempts = 5

#The following shows the number of attempts to enter the passworrd the user has already made.
attempts = 0

#Here we will use the WHILE LOOP to repeadtly as the user the password until 5 attempts are over for the user.
while attempts < max_attempts:
    
    enter_pass= input("Please enter the password: ")
    
    # Check if the entered password is correct
    if enter_pass == correct_pass:
        print("Password correct! Access granted.")
        break  # Exit the loop when the correct password is entered
    else:
        attempts += 1
        rem_attempts = max_attempts - attempts
        if rem_attempts > 0:
            print(f"Incorrect password. You have {rem_attempts} attempts remaining.")
        else:
            print("Incorrect password. You have reached the maximum number of attempts.")
            print("Authorities have been alerted.")
            break  # Exit the loop after the maximum attempts
