# def is_prime(number):
#     if number < 2:
#         return (False)
#     for i in range (2, int(number**0.5) +1):
#         if number % i ==0:
#             return (False)
#     return (True)
# num = int(input("Please enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

num = int(input("Enter a number: "))

name = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            name = True
            break

    if name:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")



