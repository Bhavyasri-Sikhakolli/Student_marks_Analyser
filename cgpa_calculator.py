name=input("Enter Student name:")
num_subjects=int(input("Enter number of subjects:"))
total_grade_points=0
for i in range(num_subjects):
    grade_point=float(input(f"Enter grade point for subjects {i+1}:"))
    total_grade_points+=grade_point
cgpa=total_grade_points/num_subjects
print("\n----Student Result----")
print("Student name:",name)
print("CGPA:",round(cgpa,2))