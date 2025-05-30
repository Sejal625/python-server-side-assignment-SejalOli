# 2      Create a program that takes a list of students names and stores them in a file. 
# Then, read the file and display the contents

students=[]

n=int(input("Enter the number of students"))
for i in range(n):
    Name=input("Enter the name of student")
    students.append(Name)
with open("student.txt",'w') as file:
    for Name in students:
        file.write(Name +"\n")
    print("\nstudents")
with open("student.txt",'r') as file:
    x=file.read()
    print(x)
