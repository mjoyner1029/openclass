# task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades)

# task 2
def Average(grades): 
     sum(grades) / len(grades)
average = Average(grades) 
print("Average of the list =", (average))

# task 3 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()

new_grades = ["failed" if x < 80 else x for x in grades]

print(new_grades)
