# Assignment Week 3
#   Write a program that asks a user to input a string and outputs every second letter in reverse order.

#   $ python secondstring.py
#   Please enter a sentence: The quick brown fox jumps over the lazy dog.
#   .o zletrv pu o wr cu h

sentence = str(input("Input a string:"))
sentenceReversed = sentence[::-2]
print(sentenceReversed)

# Create variable (sentence) which asks user to input a string
# Create second variable which reverses (or slices) the input and steps back every 2 letters
# Reference taken from https://www.w3schools.com/python/python_howto_reverse_string.asp
# Print this reversed variable
