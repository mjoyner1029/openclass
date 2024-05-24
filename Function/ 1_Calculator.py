# task 1
import math

# this function adds 2 number
def addition(num1, num2):
    return(num1 + num2)

# this function subtracts 2 number
def subtraction(num1, num2):
    return(num1 - num2)

# this function multiplies 2 number
def multiplication(num1, num2):
    return(num1 * num2) 

# this function divides 2 number
def division(num1, num2):
    return(num1 / num2)

print("Please select operation -\n" \
		"1. addition\n" \
		"2. subtraction\n" \
		"3. multiplication\n" \
		"4. division\n")

select_choice = int(input('select the operation type 1, 2, 3, 4:'))



if select_choice == 1:
	print(num1, "+", num2, "=",
			addition(num1, num2))

elif select_choice == 2:
    print(num1,'-', num2, '=', 
          subtraction(num1, num2))
    
elif select_choice == 3:
    print(num1,'*', num2, '=', 
          multiplication(num1, num2))

elif select_choice == 4:
    print(num1,'/', num2, '=', 
          division(num1, num2))

else:
    print('invaild choice')
