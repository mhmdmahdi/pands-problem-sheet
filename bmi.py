weight = int(input("Enter weight(kg):"))
print(weight)
# define variable weight
# ensure this variable is set up as an integer
# take in variable from terminal using input function
# return this input using print function

height = int(input("Enter height(cm):"))
print(height)

bmi = weight / ((height / 100) ** 2)
print(round(bmi, 2))
# bmi = kg/m^2
# round the float value to 2 decimal places
