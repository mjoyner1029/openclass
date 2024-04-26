# task 1
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])

# task 2
temperatures_under = [i for i in temperatures if i < 100]
print(temperatures_under)

#task 3
temperatures.reverse()

print('Reversed List:', temperatures[4:9])