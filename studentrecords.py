"""3 Implement a program to store student records(name,roll,marks,contact number) using a dictionary.   
a Provide a menu options to add,search,and display students"""


students = {}

def Add():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student with this roll number already exists.")
        return
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    contact = input("Enter Contact Number: ")
    students[roll] = {
        'name': name,
        'marks': marks,
        'contact': contact
    }
    print("Student added successfully.\n")

def search():
    roll = input("Enter Roll Number to Search: ")
    if roll in students:
        print(f"\nStudent Found")
        for key, value in students[roll].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Student not found.\n")

def Display():
    if not students:
        print("No student records to display.\n")
    for roll, info in students.items():
        print(f"\nRoll: {roll}")
        for key, value in info.items():
            print(f"{key}: {value}")

def main():
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            Add()
        elif choice == '2':
            search()
        elif choice == '3':
            Display()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
 main()
