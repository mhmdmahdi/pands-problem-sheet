# Function to return the square root of
# a number using Newtons method
def sqrt(n, l):
    # * function named sqrt is being created and using tuple unpacking to create two set variables on one line of code similar to Jupyter Notebook for Fibonacci Sequence in lecture.

    # Assuming the sqrt of n as n only
    x = n

    # To count the number of iterations
    count = 0

    while (1):
        count += 1

        # Calculate more closed x
        root = 0.5 * (x + (n / x))

        # Check for closeness
        if (abs(root - x) < l):
            break

        # Update root
        x = root

    return root
# * The logic for this code which I believe is not necessary to understand is explained in the referenced site below


# Driver code
if __name__ == "__main__":
    # * _______________________________________________________________________________________________

    # All of the above code contributed by AnkitRai01
    # * code reference https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.
    # * Any comments with a single '#' is the comment taken from the referenced site
    # * Any comments with '# * ' are my own comments

    n = float(input("Please input a positive integer:"))
    while (n < 1):
        n = float(input("Please input a positive integer:"))
    l = 0.00001
# * This while loop ensures that only a postive float number can be inputted. Any negative values or 0 will not be accepted. Loop continues until positive number is inputted.
# * 'n' is the input which is fed into the function 'sqrt'
    print(sqrt(n, l))
