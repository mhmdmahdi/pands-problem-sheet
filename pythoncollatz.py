integer = int(input("Please input a positive integer:"))
while (integer <= 0):
    integer = int(input("Please input a positive integer:"))

x = integer

while x > 1:
    if (x % 2 == 0):
        x = (round(x / 2))
# reference to round integer to whole numbers https://kodify.net/python/math/round-integers/
    elif (x % 2 == 1):
        x = ((x * 3) + 1)
    print(x)
