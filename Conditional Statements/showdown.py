# task 1
first_number = int(input("please pick a number :"))
second_number = int(input("please pick a second number :"))
third_number = int(input("please pick a third number :"))

if(first_number > second_number) and (first_number > third_number):
   largest = first_number
elif(second_number > first_number) and (second_number > third_number):
   largest = second_number
else:
   largest = third_number

print("The largest number is", largest)

if(first_number < second_number) and (first_number < third_number):
   smallest = first_number
elif(second_number < first_number) and (second_number < third_number):
   smallest = second_number
elif(third_number < first_number) and (third_number < second_number):
   smallest = third_number

print("The smallest number is", smallest)

if(first_number == second_number):
   equals = first_number and second_number
elif(second_number == third_number):
   equals = second_number and third_number
elif(third_number == first_number):
   equals = third_number and first_number
print("both numbers are the same",equals)

if(first_number == second_number == third_number):
   equals = third_number and first_number and second_number
   print("all numbers are the same", equals)