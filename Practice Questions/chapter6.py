#Question 1 -  Write a Python program that uses a while loop to print the even numbers from 2 to 10.
num = 2
while num <= 10:
    print(num)
    num += 2

#Question 2 - Write a Python program that uses a for loop to print the numbers from 1 to 10.
for numbers in range(1, 11):
    print(numbers)

#Question 3 - Write a Python program that uses a loop to find the sum of all the numbers from 1 to 100.
sum_result = 0
for number in range(1, 101):
    sum_result += number

print("Sum of numbers from 1 to 100:", sum_result)

#Question 4 - Write a Python program that uses the break statement to exit a for loop when a specific condition is met.
for digit in range(1, 11):
    if digit == 5:
        break
    print(digit)

#Question 5 - Write a Python program that uses a while loop to find the largest number among a series of 
#user-input values until they enter '0' to exit the loop
largest_num = float('-inf')
while True:
    user_input = float(input("Enter a number (enter '0' to exit): "))
    if user_input == 0:
        break
    if user_input > largest_num:
        largest_num = user_input

print("The largest number entered:", largest_num)