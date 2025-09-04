'''Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''

# Solution 1

dic = {"Avi" : 100,"Pratham" : 99.99, "Manas ": 98 , "Sarvesh ": 97, "Mohit ": 96}

# Solution 2
name = input("Enter your name : ")

# Solution 3
if (name in dic):
    print(f"{name}'s marks are: {dic[name]}")

# Solution 4

else:
    print("Sorry! Student not found in the record.")

