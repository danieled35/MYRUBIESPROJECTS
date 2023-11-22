# You have a set of test scores, and you want to calculate the average score. Write a Python function to calculate and return the average of these test scores.
# Instructions:

# 1. Create a Python function called calculate_average_score that takes a list of test scores as its parameter.
# 2. Inside the function, calculate the sum of the test scores in the list.
# 3. Divide the sum by the number of test scores to calculate the average.
# 4. Return the calculated average from the function.
# 5. Call the function with different sets of test scores and print the results.


def calculate_average_score(test_scores):
    # name=1,2,3,4,5,6,7
    ment=(sum(mytuple)/len(mytuple))
    print(mytuple)
    return(ment)
mytuple=(1,2,3,4,5,6,7,8,9)

print(calculate_average_score(mytuple))

