#A movie theater charges different ticket prices depending on a person’s age. 
#If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; 
#and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
#age, and then tell them the cost of their movie ticket

age_checking = ("Greetings! Welcome to G's Cinemas. Before entering, we require visitors to enter their age. \nIf you wish to leave, please type 'quit': ")

while True:
    age = input(age_checking)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Congratulations! People aged below three get the ticket for free. Welcome once again!")
    elif age < 13:
        print("Congratulations! Your ticket will be priced at only 10$. Welcome!")
    else:
        print("Welcome! Your ticket will be priced at 15$.")