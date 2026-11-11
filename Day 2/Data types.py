#Data types

#Strings

"Hello"[0] #This will return the first character in the string, which is H

#In a string of characters, you can pull out each character individually
print("Hello"[4]) #This will return the last character in the string, which is o
print("Hello"[0]) #programmers always start counting from zero (0), because we work with binary (0, 1)
#the method of pulling out a particular character from a string is called subscript
#"123" is a string, not a number. This is because of the double quotes ""
print("123" + "345") #This will return 123345, not 468.

#Integer

#programming lingo for whole numbers (no decimal place)
print(123 + 345) #This will return 468, because these are numbers, not strings.

#Large intergers

#rather than separating large numbers with commas, we can use underscores to make them more readable
#123,456,789 is the same as 123_456_789

#Float

#programming lingo for numbers with decimal places
print(3.14159) #This will return 3.14159

#Boolean

#programming lingo for True or False
True
False
#these values start with capital letters, and are not surrounded by quotes.

#Type checking

#type() #This is a function that allows us to check the data type of a value

#type casting

#to change a value from one data type to another, we can use type casting.
str() #This is a function that converts a value to a string
int() #This is a function that converts a value to an integer
float() #This is a function that converts a value to a float
name = input("What is your name? ")
num_char = len(name)
print("Your name has " + str(num_char) + " characters.") 
#This will return the number of characters in your name.
