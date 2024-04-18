# task 1
num1 = int(input("please pick a number"))
num2 = int(input("please pick a second number"))
num3 = int(input("please pick a third number"))

if(num1 >= num2) and (num1 >= num3):
   largest = num1
elif(num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

if(num1 <= num2) and (num1 <= num3):
   smallest = num1
elif(num2 <= num1) and (num2 <= num3):
   smallest = num2
elif(num3 <= num1) and (num3 <= num2):
   smallest = num3

print("The smallest number is", smallest)

if(num1 == num2):
   equals = num1 and num2
elif(num2 == num3):
   equals = num2 and num3
elif(num3 == num1):
   equals = num3 and num1
   print("both numbers are the same",equals)

if(num1 == num2 == num3):
   equals = num3 and num1 and num2
   print("all numbers are the same", equals)