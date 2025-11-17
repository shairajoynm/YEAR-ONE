import os
print("----------------------------------------")
print("Student Information System")
print("----------------------------------------")

student_list = {}

while True:
    print("Choose what you want to do \n a - Add Information \n b - Search a Record \n c - Delete a Record \n d - Review the Record")

    choosing = input(" =--> ").lower()
    
    if choosing == 'a':
        id = eval(input("Student ID number:  "))
        last_name = input("Last name: ").lower
        first_name = input("First name: ").lower
        course = input("Program: ")

        student_list = {id:[last_name, first_name, course]}

        print("\nRecord Saved\n")
        

