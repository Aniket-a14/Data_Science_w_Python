#Write a python program that takes an array of students grade and returns the average grade. Based on the average grade, it then assigns a letter grade to the student. The grade scale is as follows:

#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

#Example: [88, 99, 70, 100, 90, 80, 85, 60, 30] 
#Average grade: 77.5
#Letter grade: C


import numpy as np

def average_grade(grades):
    avg = np.mean(grades)
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


num = int(input("Enter number of students: "))
student_grades=[]

for j in range(num):
    grades = list(map(int, input(f"Enter grades of student {j+1}: ").split()))
    student_grades.append(grades)
    print(f"Student {j+1} average grade: {np.mean(grades):.2f}")
    print(f"Student {j+1} letter grade: {average_grade(grades)}")

student_grades = np.array(student_grades)
print(student_grades)
print(type(student_grades))