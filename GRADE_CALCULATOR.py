def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
n=int(input("how many marks?"))
for i in range(n):
    score = float(input("Enter your score: "))
    grade = calculate_grade(score)
    print(f"Your grade is: {grade}")
