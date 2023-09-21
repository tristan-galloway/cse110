import math

"""

team: Unathletic Avengers
teacher: brother keers
file: "shapes"
assignment: 
Write a program to compute the areas of three different shapes. 

Prompt for the necessary information, then compute and display the area, as follows:

Make sure that your program can appropriately handle decimal values as well as whole numbers.

1. Square—The area is the length of a side squared.

2. Rectangle—The area is the length multiplied by the width.

3. Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.

"""

# Ask the user for the side length of their sqaure in centimeters
side = float(input(f"Please enter the length of one side of the square in centimeters: "))

# Ask the user for the side length of their rectangle in centimeters
length = float(input(f"Enter the length of the rectangle in centimeters: "))
width = float(input(f"Enter the width of the rectangle in centimeters: "))

# Ask the user for the side length of their circle in centimeters
circle = float(input(f"Enter the radius of the circle in centimeters: "))

# Make the string we will print later to return the calculations to the user
calc = f"""

The area of your square is {side ** 2:.3f}cm^2 or {side ** 2/ 10000:.3f}m^2

The area of your cube is {side ** 3:.3f}cm^2 or {side ** 3 / 10000:.3f}m^2

The area of your rectangle is {length * width:.3f}cm^2 or {length * width / 10000:.3f}m^2

The area of your circle is {math.pi * circle ** 2:.3f}cm^2 or {math.pi * circle ** 2 / 10000:.3f}m^2

The area of your sphere is {4 * math.pi * circle ** 2:.3f}cm^2 or {4 * math.pi * circle ** 2 / 10000:.3f}m^2

"""

# Print the multi line string directly above
print(calc)