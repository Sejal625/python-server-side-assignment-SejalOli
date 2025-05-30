"""5 Write Python code to read from a CSV filr of student marks and calculate 
average marks."""

import csv
def Average_Marks(filename):
    with open(filename, newline="") as file:
        readstudent = csv.DictReader(file)
        Marks_Averages = {}
        for row in readstudent :
            name =row['Name']
            marks = []
            for subject in row:
                if subject !='Name':
                    marks.append(int(row[subject]))
            #marks = [int(row[subject])] for subject in row if subject !='Name
            average = sum(marks)/len(marks)
            Marks_Averages[name] = average
        return Marks_Averages
    

filename ='student.csv'
avg_marks = Average_Marks(filename)

print("Average marks of each student: ")
for name, avg in avg_marks.items():
    print(f"{name} :{avg} ")