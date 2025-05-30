"""6 Develop a simple OOP based python class Student with attributes like name, roll number, and marks.
Implement methods to input and display details"""

class Student:
    def __init__(self):       #_init_ method is used to initializes the attributes of the student class
        self.name = ""
        self.roll_number = ""
        self.marks = []

    def input_details(self):    #input_details method is used to Takes user input for name, roll number, and marks.
        self.name = input("Enter student name: ")
        self.roll_number = input("Enter roll number: ")
        total_subject = int(input("Enter number of subjects : "))
        self.marks = []
        for i in range(total_subject):
            mark = int(input(f"Enter the marks subject {i + 1 } : "))
            self.marks.append(mark)

    def display_details(self):   #display_details method is used toPrints the student's details
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

student1 = Student()
student1.input_details()
student1.display_details()
