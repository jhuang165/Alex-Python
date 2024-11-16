"""
fav_number = input("What's your favorite number? ")

if fav_number.isdigit() == False:
    print("That's not a number!")
else:
    print("Your favorite number is " + fav_number)

num = 5

while num < 10:
    num += 1
    print(num)
"""

def helloworld():
    print("hello world")

# helloworld()
def hellocomputer(name, color):
    print("hello " + name)
    print("your favorite color is " + color)

hellocomputer("alex", "blue")

"""
Write a function called favorite_book() that accepts one parameter,
title. The function should print a message, such as One of my favorite books is Alice in
Wonderland. Call the function, making sure to include a book title as an argument in the
function call.
"""

def favorite_book2(title):
    print("One of my favorite books is " + title + ".")

favorite_book2("Great Gatsby")

def favorite_book(author, book):
    print("hello your favorite authors is " + author)
    print("hello your favorite book is " + book)
favorite_book("Alexander Dumas", "count of monte cristo")

favorite_book(book="The Handmaid's Tale", author="Margaret Atwood")

favorite_book(book="harry potter", author= "JK Rowling")
def favorite_color(color="blue"):
    print("your favorite color is " + color)

favorite_color("green")

"""
Write a function called make_shirt() that accepts a size and the text of a message
that should be printed on the shirt. The function should print a sentence summarizing the size of
the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second
time using keyword arguments.
"""
def make_shirt(size="XL", message="sup"):
    #print("Your size is " + size )
    #print("Your print is " + message)
    print(f"Your size is {size}")
    print(f"Your printed message is {message}")

make_shirt(" L ")
make_shirt(message="supreme", size="M")
make_shirt(message="supreme", size="M")