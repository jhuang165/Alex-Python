"""
Restaurant: Make a class called Restaurant. The __init__() method for Restaurant
should store two attributes: a restaurant_name and a cuisine_type. Make a method called
describe_restaurant() that prints these two pieces of information, and a method called
open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually,
and then call both methods.
"""

class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(self.name)
        print(self.type)
    
    def open_restaurant(self):
        print(f"{self.name} is now open for business!")

restaurant = Restaurant("Panda Express", "Chinese (fake)")

print(f"My restaurant is called {restaurant.name}, and it serves {restaurant.type} food")

restaurant.describe_restaurant()
restaurant.open_restaurant()

"""
Three Restaurants: Start with your class from Exercise 9-1. Create three different
instances from the class, and call describe_restaurant() for each instance."
"""

restaurant2 = Restaurant("outback", "Aussie")

restaurant2.describe_restaurant()

restaurant3 = Restaurant("Mcdonalds", "American")

restaurant3.describe_restaurant()

restaurant4 = Restaurant("beans on toast", "English")

restaurant4.describe_restaurant()


"""
Users: Make a class called User. Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile. Make a method
called describe_user() that prints a summary of the user’s information. Make another method
called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user."
"""  
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name 
        self.age= age
    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)

    def greet_user(self):
        print(f"hi my name is {self.first_name} my surname is {self.last_name}, i am {self.age} years old.")
        
user = User("Alex","Chang","15")

user.describe_user()
user.greet_user()