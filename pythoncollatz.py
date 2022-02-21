integer = int(input("Please input a positive integer:"))
while (integer <= 0):
    integer = int(input("Please input a positive integer:"))
# this while loop ensures that only a postive integer which is not 0 can be inputted. Any negative values or 0 will not be accepted.

x = integer

while x > 1:
    if (x % 2 == 0):
        x = (round(x / 2))
# reference to round integer to whole numbers https://kodify.net/python/math/round-integers/
    elif (x % 2 == 1):
        x = ((x * 3) + 1)
    print(x)
# if/ elif statement within while loop to continue iterations to completion. Code completes once final result of 2 is reached as this is greater than 1 and once divided by 2 gives a result of 1
# modulus is used to determine if the value inputted is odd or even as described in the Week 4 lectures
