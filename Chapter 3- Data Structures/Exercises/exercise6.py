# oh no there is no space in the table it is too small :(

names = ['James Murray', 'Sal Vulcano', 'Brian Quinn']

stmt1 = f"Greetings, {names[0]}, of the Impractical Jokers! I would like to formally invite you to a dinner feast."
stmt2 = f"Greetings, {names[1]}, of the Impractical Jokers! I would like to formally invite you to a dinner feast."
stmt3 = f"Greetings, {names[2]}, of the Impractical Jokers! I would like to formally invite you to a dinner feast."
print(stmt1)
print(stmt2)
print(stmt3)

#Sal is not available. Let's invite their friend Joe Gatto.
print(f"Sorry, {names[1]} will be unavailable for this dinner.")
del(names[1])
names.insert(1, 'Joe Gatto')

#Resending the invitations
stmt1 = f"Greetings, {names[0]}, of the Impractical Jokers! I would like to formally invite you to a dinner feast."
stmt2 = f"Greetings, {names[1]}, of the Impractical Jokers! I would like to formally invite you to a dinner feast."
stmt3 = f"Greetings, {names[2]}, of the Impractical Jokers! I would like to formally invite you to a dinner feast."
print(stmt1)
print(stmt2)
print(stmt3)

# There's no room for this much people on the table!! We need only two people
print(f"\nApologies, Impractical Jokers, it seems there is not enough room for all of you at the table.")

newguest = names.pop(2)
print(f"Apologies, {newguest}. Unfortunately, there isn't enough room.")

# Two people are now remaining on the list. That should fit the space available.
newguest = names[0]
print(f"{newguest}, a seat is now reserved for you at this dinner feast. Please attend.")
newguest = names[1]
print(f"{names[1]}, a seat is now reserved for you at this dinner feast. Please attend.")


