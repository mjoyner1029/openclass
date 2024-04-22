Grade = input("what is your is your grades(A/B/C):")
sports = input("do you participate in sports(yes/no):")
drama = input("do you participate in drama:")

discount = 0

if Grade == "A":
    if sports == "yes":
        discount = 20
    else:
        discount = 10
elif Grade == "B":
    if drama == "yes":
        discount = 15
        
print(f"your discount will be be {discount}% discount.")