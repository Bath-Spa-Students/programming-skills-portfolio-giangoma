#Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, 
#print everything you know about each pet
 
kennel1 = {'animal':'Shih Tzu','owner':'Gabbie'}
kennel2 = {'animal':'German Shepherd', 'owner':'Aviona'}
kennel3 = {'animal':'Maltipoo', 'owner':'Yzach'}
kennel4 = {'animal':'Havanese','owner':'Craig'}

pets = [kennel1, kennel2, kennel3, kennel4]
for kennel in pets:
    print(f'This {kennel["animal"]} is owned by {kennel["owner"]}.')

