# task 1
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

stu_1 = students[2]
gra_1 = grades[2]
act_1 = activities[2]

combined = [stu_1, gra_1, act_1]
print(f"The student is: {combined}")

#task 2
for (students_approved) in zip(students,grades,activities):
    students_approved = [i for i in students if i != 'Jane']
print(students_approved)