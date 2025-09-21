# pattern_drawing.py
# Program to draw a square pattern using while and nested for loops

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to go through rows
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # After finishing a row, print newline
    print()
    row += 1
