#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(shirtsize = 'large', shirtmsg = 'I Love Python'):
    print(f"\nI'm going to make a {shirtsize}-sized shirt.")
    print(f"\nThe shirt will say, '{shirtmsg}'.")

make_shirt()
make_shirt(shirtsize = 'medium')
make_shirt('small', 'Creative Computing')