class Human:
    def __init__(self, name, age, sex, race, height):
        self.name = name
        self.age = age
        self.sex = sex
        self.race = race
        self.height = height
    
    def introduction(self):
        print(f"My name is {self.name}, I am {self.age} years old, I am {self.sex}, {self.race}, and my height is {self.height}.")


person = Human("alex", 14, "male", "asian", "5'11")

person.introduction()

person_2 = Human("Jeffrey", 20, "male", "asian", "5'7")
person_2.introduction()


person1= Human("Lebron", 41, "female", "Black", "6'9")
person1.introduction()

person_3= Human("lamelo", 24, "male", "light skin", "6'7")
person_3.introduction()
