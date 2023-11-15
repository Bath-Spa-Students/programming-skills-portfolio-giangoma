#Question 1 - Write a python program with if statement that assigns 20 to the variable y and assigns 40 to the variable z if the 
#variable & is greater than 100.

y = 160
z = 0

if y > 100:
    z = 40

# Print the values of y and z
print("Value of y:", y)
print("Value of z:", z)

#Question 2 - Write an if-else statement that assigns O to the variable b if the variable a is less than 10.
#Otherwise, it should assign 99 to the variable b.

a = 56
b = 0

if a < 10:
    b = 0
else:
    b = 99

# Print the value of b
print("Value of b:", b)

#Question 3 - Write a python program with nested decision structures that perform the following: If amount1
#is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2

amount1 = 60
amount2 = 75

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print("The greater amount is ", amount1)
    else:
        print("The greater amount is ", amount2)

#Question 4 - Write a python program with an if-else statement that displays Speed is normal if the speed
#variable is within the range of 24 to 56. If the speed variable's value is outside this range, display 'Speed is abnormal'

speed = 70

if 24 <= speed <= 56:
    print("Speed is normal")
else:
    print("Speed is abnormal")

#Question 5 - Write a Python program that uses the elif statement to determine the season based on the
#month provided as input.

month = 7

if 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Fall")
else:
    print("Winter")