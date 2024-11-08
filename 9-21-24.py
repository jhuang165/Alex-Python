

# Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary

yuoi = {"first_name": "Eric truck", "last_name": "陈", "age": "14", "city": "Shanghai"}

print(yuoi["first_name"])

yuoi["color"] = "black"

del yuoi["color"]

print(yuoi.get("fist_name", "don't know"))
"""
for key in sorted(yuoi.keys()):
    print("key: " + key + " value: " + yuoi[key])
"""

# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous chapters. Use these
# words as the keys in your glossary, and store their meanings as values

# Print each word and its meaning as neatly formatted output. You might print the word followed
# by a colon and then its meaning, or print the word on one line and then print its meaning
# indented on a second line. Use the newline character (\n) to insert a blank line between each
# word-meaning pair in your output.
keys = {"pop": "delete", "orgin": "0", "append": "Insert", "list": "group", "string": "latin words"}
for key in sorted (keys.keys()):
    print("key: " + key + "  value: " + keys[key])