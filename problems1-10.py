# Project Euler 1-10

print 'Project Euler: #1 - 10'

# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of the multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def one(x):
    sum = 0
    for num in range(0,x):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum

print 'Problem 1:', one(1000)

# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms.
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

def two(lim):
    first, next = 0, 1
    sum = 0
    while first < lim:
        if not first % 2:
            sum += first
        first, next = next, first + next
    return sum

print 'Problem 2:', two(4000000)

# Problem 3
# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143?

def three(num):
    fac = 2
    while fac < num:
        while num % fac == 0:
            num = num / fac
        fac += 1
    return fac

print 'Problem 3:', three(600851475143)
