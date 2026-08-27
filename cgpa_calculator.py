n = int(input("Enter number of subjects: "))

total_points = 0
total_credits = 0

for i in range(n):
    grade_point = float(input(f"Enter grade point for subject {i + 1}: "))
    credits = float(input(f"Enter credits for subject {i + 1}: "))

    total_points += grade_point * credits
    total_credits += credits

cgpa = total_points / total_credits

print(f"Your CGPA is: {cgpa:.2f}")