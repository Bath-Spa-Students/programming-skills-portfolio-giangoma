#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.

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





