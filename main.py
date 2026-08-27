import csv
import os


name = input("Enter Student name:")
subjects = ["Python", "DBMS", "Math" ,"English", "Computer"]
marks = []
for i in subjects:
    mark = float(input(f"Enter marks for {i}:"))
    marks.append(mark)
total = sum(marks)
avg = total / len(marks)
if avg >= 90:
    grade='A+'
elif avg >= 80:
    grade='A'
elif avg >= 70:
    grade='B'
elif avg >= 60:
    grade='c'
elif avg>=50:
    grade='D'
else:
    grade='F'
result="PASS" if avg>=40 else "FAIL"
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average marks: {avg:.2f}")
print(f'Grade: {grade}')
print(f'Result: {result}')

file_name="Student_results.csv"
file_exists = os.path.exists(file_name)
with open(file_name, "a", newline='') as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Student Name",
            "Total Marks",
            "Average",
            "Grade",
            "Results"
        ])
    writer.writerow([
        name,
        total,
        round(avg, 2),
        grade,
        result
    ])
print("\nResult has been saved to Student_results.csv")