#Make a dictionary containing three major rivers and the country each river runs through.
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary.

rivers = {'Ganges':'India',
          'Danube':'Europe',
          'Thames':'England'}
for key, value in rivers.items():
    print("The", key, "river runs through", value)
for key, value in rivers.items():
    print("Rivers: ", key)
for key, value in rivers.items():
    print("COuntries: ", value)