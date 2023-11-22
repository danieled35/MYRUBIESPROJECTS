#  Exercise: Calculate Square and Square Root
# 1. Create a Python function called calculate_square that takes a number as a parameter. This function should return the square of that number, calculated as square = number * number.

# 2. Create another Python function called calculate_square_root that takes the square of a number as a parameter. This function should calculate and return the square root of the provided value.
# 3. Prompt the user to enter a number using the input() function.
# 4. Use the calculate_square function to calculate the square of the number provided by the user.

# 5. Then, use the calculate_square_root function to calculate the square root of the result from step 4.
# 6. Print the results, including the square of the number and the square root of the squared result. 

import math 
def calculate_square(number):
    square = number * number 
    return(square)
def calculate_square_root(square_of_a_number):
    root=math.sqrt(square_of_a_number)
    return(root)
User_input=int(input("Please enter a number "))
square=calculate_square(User_input)
print(f"this is the calculated sqaure {square} ")
root= calculate_square_root(square)
print(f"the calculated rooot is {root} ")



