# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def factorial(n = 1):
    if(n > 1):
        return n * factorial(n - 1)
    elif n == 1:
        return 1
    elif n == 0:
        return 0


choice = input("Enter the amount to get factorial for [Enter d for default value]:  ")
print(choice)

if choice != "d":
    print(factorial(int(choice)))
else:
    print(factorial())
