# Project Euler
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of the multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def foo(x):
    sum = 0
    for num in range(0,x):
        if num % 3 == 0:
            sum += num
        if num % 5 == 0:
            sum += num
        if num % 15 == 0:
            sum -= num
    return sum

print(foo(1000))
