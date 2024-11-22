#Let the user input their grade
score = int(input("Enter your score"))
# determining the grade on basis of the score inputted
if score >= 90:
    print('your grade is A') #A grde is given to score above 90
elif score >= 80:
    print ('Your grade is B') #B grade is given to score above 80
elif score >= 70:
    print('your grade is C') #C grde is given to score above 70
elif score >= 60:
    print('Your grade is D') #D grade is given to score above 60
else:
    print('Your grade is F') #F grade is given to score bellow 60
 