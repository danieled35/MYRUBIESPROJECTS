import math_operations

# Addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("""
Enter Operation:
+ - for addition
- for subtraction

""").strip()

operation_dict = {"+": math_operations.add,
                  "-": math_operations.subtract,
                  "*": math_operations.multiply,
                  "/": math_operations.divide}

# if operation == '+':
#     result = math_operations.add(num1, num2)
# if operation == '-':
#     result = math_operations.subtract(num1, num2)
# if operation == '*':
#     result = math_operations.multiply(num1, num2)
# if operation == '/':
#     result = math_operations.divide(num1, num2)

result = operation_dict.get(operation)
print(result)