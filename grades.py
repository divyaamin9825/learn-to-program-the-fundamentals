grade1 = 70
grade2 = 10
total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
elif grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
