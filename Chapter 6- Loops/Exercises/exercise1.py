#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.

recipe = "\nGreetings! We'd like to cook you a pizza. What toppings would you be interested in? Please type them out. \nIf you would like to opt out, please type 'quit'."

while True:
    pizza = input(recipe)
    if pizza != 'quit':
        print(f"\nThanks! We're going to cook you a pizza with {pizza} as your topping(s) of choice. Happy munching!")
    else:
        break