# Calerbe Jean Baptiste
# file name: Calerbe_GPA_App
#This program will identify which list the students will be in (Dean's or Honor Roll)
print("Hello, \n I will need your last name, first name and your GPA in order to assign you to a list")
print()
lname=input("Please enter your last name or ZZZ to quit :")
while lname!= 'ZZZ' :
    fname=input("Enter your first name :" )
    gpa=float(input("Enter your GPA:\n"))
    if gpa >= 3.5 and gpa< 4.0 :
        print("Welcome to the Dean's List",fname, lname)
    elif  gpa >= 3.25 and gpa < 3.5 : 
        print("Welcome to the Honor Roll List",fname, lname)
    else:
        print("You can not be in our lists, sorry about that", fname, lname)
    lname=input("Please enter your last name or ZZZ to quit :")