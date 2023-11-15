#Question 1 - Write a Python function that takes two numbers as arguments and returns their sum.
def add_numbers(a, b):
    return a + b

num1 = 5
num2 = 7
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")

#Question 2 - Write a Python function that calculates the factorial of a given positive integer using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
outcome = factorial(number)
print(f"The factorial of {number} is: {outcome}")

#Question 3 - Write a Python program that uses a function to check if a given number is prime or not.
def is_prime(digit):
    if digit <= 1:
        return False
    for i in range(2, int(digit**0.5) + 1):
        if digit % i == 0:
            return False
    return True

numberrr = 11
if is_prime(numberrr):
    print(f"{numberrr} is a prime number.")
else:
    print(f"{numberrr} is not a prime number.")

#Question 4 - Write a Python program that defines a function to calculate the area of a circle, and then calls that function with a given radius.
def calculate_circle_area(radius):
    return 3.14 * radius**2

circle_rad = 5
area = calculate_circle_area(circle_rad)
print(f"The area of a circle with radius {circle_rad} is: {area}")

#Question 5 -  Write a Python program that defines a function to check whether a given number is prime.
def is_prime(numm):
    if numm <= 1:
        return False
    for i in range(2, int(numm**0.5) + 1):
        if numm % i == 0:
            return False
    return True

numero = 7
if is_prime(numero):
    print(f"{numero} is a prime number.")
else:
    print(f"{numero} is not a prime number.")
