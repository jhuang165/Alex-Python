"""
# this is a demo of f-strings

number = 70
number2 = 80
message = f"she is {number}, he is {number2}"
print(message)



this is a multi-line comment
see this is more than one line


# you don't have to close it

name = "alex chang"

# print(name.title())

# print(name.upper())

name2 = "JEFFREY HUANG"

#print(name2.lower())

message = "it's sat"

#print(message.title())

name3 = "ALEX CHANG"

#print(name3.lower())

name4 = "hello      alex chang       "

print(name4.lstrip())

message2 = 'single quote message, おはようございます'

message = "\"this is a message\n\tplease don't open it'"
print(message2)
"""
# Create a variable for your name, Introduce yourself using that variable (hint: use f-strings)

name = "alex chang"
message = f"hi my name is {name}"
# print(message)

# Print your name in uppercase, lowercase, and in proper form without modifying your name directly.
name = "alex chang"
print(name.upper())


# Print a quote from a person, and include the quotes
message = "\"i came i saw i conquer\""
print(message)

# make a list of groceries, making sure that each item has its own line and is indented

message = " \tmilk\n\teggs\n\tapples\n\t"
print(message)
