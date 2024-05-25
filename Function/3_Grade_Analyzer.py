# task 1
import math

number_of_students = int(input("How man studebts are in the class?: "))
grades = int(input("what is their grades?: "))

def addition(grades):
    return(grades, sum)

def calculate_average_grade(student):
    total_grade = sum(grades)
    average_grade = total_grade / number_of_students
    return average_grade

def highest_and_lowest(grades):
    data = grades.split()
    data = [int(grades) for grade in data]
    data.sort()
    return f'{data[-1]} {data[0]}'


def lettergrade (grades):

    if grades >=90:
        print('A')
    elif grades >=80 and grades <90:
        print('B')
    elif grades >=70 and grades <80:
        print('C')
    elif grades >=60 and grades <70:
        print('D')
    else:
        print('F')
    