#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
#and then use a while loop to remove all  occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['Tuna Sandwich', 'Pastrami Sandwich' , 'PB&J Sandwich', 'Grilled Cheese Sandwich',
                   'Pastrami Sandwich', 'Meatball Sandwich', 'Croque Monsieur', 'Pastrami Sandwich']
finished_sandwiches = []

print("Sorry! The deli has run out of pastrami stock. At the moment, we cannot produce pastrami sandwiches.")
while 'Pastrami Sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami Sandwich')

print("\n")
while sandwich_orders:
    sandwich_now = sandwich_orders.pop()
    print(f"{sandwich_now} is currently being prepared. Thanks!")
    finished_sandwiches.append(sandwich_now)

print("\n")
for sandwich in finished_sandwiches:
    print(f"This {sandwich} has been successfully produced.")
