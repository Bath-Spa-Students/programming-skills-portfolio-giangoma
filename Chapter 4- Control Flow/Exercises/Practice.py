salary = 30000
if salary > 50000:
    print("rich")
else:
    print("mid")

print("BMI Calculator")
bmi1 = float(input("Enter weight in kg: "))
bmi2 = float(input("Enter height in meters: "))
bmi = bmi1/bmi2
print(bmi)
if bmi > 30:
    print("You are overweight")
else:
    print("You are not overweight")

Salary = 50000
if salary > 20:
    print("super rich")

temp = float(input("Enter current temperature: "))
if temp < 40:
    print("A little cold, isn't it?")
else:
    print("Nice weather we're having.")

earning = int(input("Enter your earning per year: "))
work_experience = float(input("Enter your work experience: "))

if earning > 30000:
    if work_experience >=2:
        print("You are eligible for loan")
    else:
        print("Sorry your work experience is less than 2 years")
else:
        print("you earn less tthan 30k")