def multiply(array):
    """Multiplication function for any Iterable"""
   


    result = 1
    for num in array:
        result *= int(num)
    return result

array_1 = (1,2,4,2)
print(multiply(array_1))  