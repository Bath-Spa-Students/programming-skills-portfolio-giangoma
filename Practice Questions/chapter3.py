#Question 1 - Given a Python list, write a program to remove all occurrences of item 20.
list1 = [5, 20, 15, 20, 25, 50, 20]

# Remove all occurrences of item 20
while 20 in list1:
    list1.remove(20)

# Print the updated list
print("List after removing all occurrences of 20:", list1)

#Question 2 - Write a statement that creates a list with the following strings: 'Einstein', Newton' , 'Copernicus', and 'Kepler'
science = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
print('Some remarkable people are', science)

#Question 3 - Assume names references a list. Write a for loop that displays each element of the list
names = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
for name in names:
    print(name)

#Question 4 - Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that copies the values in numbers to numbers2.
numbers1 = list(range(1,101))
numbers2 = numbers1.copy()
print("Copied list: ", numbers2)


#Question 5 - You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. 
#Only update the first occurrence of an item.
#Work with the given list: list1 = [5, 10, 15, 20, 25, 50, 20]
list1 = [5, 10, 15, 20, 25, 50, 20]

if 20 in list1:
    index = list1.index(20)
    list1[index] = 200

print("Updated list: ", list1)
