# Exercise 1: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
# Write your code below:
friends = ["Nils", "Eric", "Patrick", "Koki"]




# Exercise 2: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
# Write your code below:
vehicles = [ "car", "motorbike", "metro", "airplane"]


# Exercise 3: Use the list from exercise 1, and add some names to it; be sure to utilize both insert() and append(), putting them in an order that you prefer.
# Write below:
friends.insert(0, "marcus")
friends.insert(3, "bowen")
friends.append("jack")

# Exercise 4: Use the list from exercises 1 and 3; delete a friend from the list, who you are no longer close with.
# Write your code below:
del friends[5]
friends.pop()


# Exercise 5: Sort the list from the previous exercises, both alphabetically and in reverse; be sure to use the sort() function with the appropriate parameters.
# Write your code below:
list.sort()
list.reverse()
list.sort(reverse=True)


# Exercise 6: Use the list from exercise 2; print what the list would look like sorted without sorting it. Then, print the list right after to show that it in fact, remains unchanged.
# Write below:

print(sorted(vehicles))
print(vehicles)


