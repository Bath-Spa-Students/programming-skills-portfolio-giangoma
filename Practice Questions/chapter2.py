#Question 1: Write a python code that uses three variables x, y, and z with respective values 10,20 and 30. Add all the
#variables and then store the result in variable a. Print the value of a. 

x, y, z = 10, 20, 30
a = x + y + z
print("The sum of x, y, and z is", a)

#Question 2: Write a python program that takes courses marks as input and then calculates average of all the
#courses. After calculating the average, calculate the percentage of a student using total marks. Assume
#the total of all the courses marks is 500 or take the total marks from the user as input. 

allcourses = int(input("Enter the total number of courses: "))
allmarks = int(input("Enter the total marks: "))

# Input course marks
marks = [float(input(f"Enter marks for Course {i + 1}: ")) for i in range(allcourses)]

# Calculate average
average = sum(marks) / allcourses

# Calculate percentage
percentage = (sum(marks) / (allcourses * allmarks)) * 100

print(f"Average marks: {average}")
print(f"Percentage: {percentage}%")

#Question 3: Write a python program that takes an input 5 from user and then type cast those values to string, int
#and float in the separate variables. Print all the variables.

user_input = input("Enter a number: ")
x_str = str(user_input)
x_int = int(user_input)
x_float = float(user_input)

print(f"String: {x_str}")
print(f"Integer: {x_int}")
print(f"Float: {x_float}")

#Question 4: Write a python program that stores an integer and string value to variables x and y. Print the type of
#variable x and y. 
x = 10
y = "Hello"

print(f"Type of x: {type(x)}")
print(f"Type of y: {type(y)}")

#Question 5: Write a python program that stores fruit names in a list named fruits. Unpack the list into three
#variables x, y and z and then print the values of each variable.
fruits = ["Apple", "Banana", "Orange"]
x, y, z = fruits

print("Value of x:", x)
print("Value of y:", y)
print("Value of z:", z)
