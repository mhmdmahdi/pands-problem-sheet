import sys
# This is a library called 'sys' that has a lot of system relevant functions

filename = sys.argv[1]
print(sys.argv)
# This is the values of the argument passed to the python programme.
print("filename is: " + sys.argv[1])
# Reference for passing arguments/parameters via command line in python taken from https://www.youtube.com/watch?v=igvoTek4efQ

with open(filename, "r") as f:
    data = f.read()
# Taken from Week 7 lecture using the 'with' command and defining the filename as a variable 'f'
# The variable 'data' then reads the file into this code using the 'r' function


def letterFrequency(f, letter):
    return data.count(letter)
# this function returns the letter count using the built in 'count()' method
# explicit function to return the letter count


print("Number of e\'s equals:", letterFrequency(f, 'e'))
# The above def and print functions are referenced from https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

# First assumption if that the user is in the directory where all of the files are saved
# Second assumption is that the txt file to be read is saved in the same directory as the programme to be ran and is also saved exactly as per the defined syntax e.g. "moby-dick.txt".
# Third assumption is that the user will also input the filename with no spelling errors and exactly as the file is saved.
# Final assumption is that the user will input the arguments into the command line to run the programme as 'python es.py moby-dick.txt'
