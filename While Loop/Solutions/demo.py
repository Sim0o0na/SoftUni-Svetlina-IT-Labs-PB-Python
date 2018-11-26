# read name
name = input()
# while classes < 12
classes = 1
sum_grades = 0
while classes <= 12:
    grade = float(input())
    if grade >= 4:
        sum_grades += grade
        classes+=1

print(f"{name} graduated. Average grade: {sum_grades / 12}")