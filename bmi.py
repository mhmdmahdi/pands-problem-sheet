weight = int(input("Enter weight(kg):"))
print(weight)
# define variable weight
# ensure this variable is set up as an integer
# take in variable from terminal using input function
# return this input using print function
# ref for understanding variable definition and input logic https://www.geeksforgeeks.org/taking-input-in-python/
# formula for printing the input as well as setting it up as an integer referenced from https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/

height = int(input("Enter height(cm):"))
print(height)

bmi = weight / ((height / 100) ** 2)
print(round(bmi, 2))
# bmi = kg/m^2 (ref https://www.wikihow.com/Calculate-Your-Body-Mass-Index-(BMI))
# round the float value to 2 decimal places (ref https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python)
