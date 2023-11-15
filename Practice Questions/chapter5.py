#Question 1 - Use a dictionary to store information about yourself.
identification = {
    'name': 'Joseph Gianne',
    'age': 16,
    'location': 'Dubai, UAE',
    'occupation': 'Student'
}

print(identification)

#Question 2 - Write a Python program to iterate through the keys of a dictionary and print them.
for key in identification.keys():
    print(key)

#Question 3 - Write a Python program to iterate through the values of a dictionary and print them.
for value in identification.values():
    print(value)

#Question 4 - Write a Python program to iterate through both the keys and values of a dictionary and print them.
for key, value in identification.items():
    print(f"{key}: {value}")

#Question 5 -  Write a Python program to merge two dictionaries into one.
city1 = {'Busan': 'South Korea', 'Ontario': 'Canada'}
city2 = {'Dubai': 'UAE', 'Quezon City':'Philippines'}

merged = city1.copy()
merged.update(city2)

print("Merged dictionary: ", merged)