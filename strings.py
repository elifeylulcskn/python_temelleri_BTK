name = 'Strings'
surname = 'Module'
age = 36

length_of_name = len(name)  # This line calculates the length of the name variable and stores it in a new variable called length_of_name.
print("My name is " + name + " " + surname + " and I am " + str(age) + " years old.")  # This line will raise an error because age is an integer and cannot be concatenated with strings directly.

greeting = "My name is " + name + " " + surname + " and I am " + str(age) + " years old."  
# This line concatenates the strings and converts the age variable to a string before concatenation.

print("My name is {} {} and I am {} years old.".format(name, surname, age))  # This line uses the format method to insert variables into the string.
print(len(name))  # This line prints the length of the name variable.   

# print(greeting)  # This line prints the greeting string.
#print(greeting[0])  # This line prints the first character of the greeting string.
#print(greeting[3])  # This line prints the fourth character of the greeting string.
#print(greeting[length-1])
#print(greeting[length_of_name - 1])  # This line prints the last character of the greeting string.
#print(greeting[0:5])  # This line prints the first five characters of the greeting string.
#print(greeting[3:10])  # This line prints the characters from index 3 to index 9 of the greeting string.

print(greeting[2:40:2])  
# This line prints every second character from index 2 to index 39 of the greeting string.