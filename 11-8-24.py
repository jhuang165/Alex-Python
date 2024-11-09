
"""
name = input("What's your name? ")

print("Hello " + name)

statement = input("Where are you from? ")

print("Hello to you in " + statement)


number = int(input("What is your favorite number? "))

print(number + 2)


num = 11


while num < 20:
    num += 2
    if num % 2 == 1:
        continue
    #ANY CODE AFTER CONTINUE WILL BE SKIPPED, AND THE CONDITION WILL BE CHECKED AGAIN

print(num)

num = 3
while num <= 30:
    print(num)
    num += 3
"""

# Ask the user for their guess
# store that number
# compare that number to our favorite number: if it is equal, then say they won, if not, then ask them to guess again

fav = 14

while True:
    guess = input("guess my age from 1-100 ")
    if guess.isdigit() != True:
        print("Please enter a number!")
        continue
    guess = int(guess)
    if guess == fav:
        print(" wow great job")
        break 
    else:
        if guess > fav:
            print("I'm younger than that!")
        else:
            print("I'm older than that!")
    
