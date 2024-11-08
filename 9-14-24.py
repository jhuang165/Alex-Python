# Review: If statements

typhoon = False

if typhoon == True:
    print("I am skipping the swim meet")
else: 
    print("I am going to the swim meet")

good_grade = True

if good_grade == True:
    print("I wont be sad")
else:
    print("My mom will get mad at me")

grade = 95

if grade >= 93:
    print("I got an A")
elif grade >= 90:
    print("I got an A-")
elif grade >= 80:
    print("I got a B")
else:
    print("I failed")

# Dictionaries

frens = {"amy": "freestyle", "austin": "butterfly", "sebastian": "backstroke"}

print(frens["austin"])

frens["austin"] = "freestyle"

swim_friends = {"Ben": "breaststroke", "Reina": "butterfly", "Eric KC": "freestyle"}

swim_friends["Graham"] = "backstroke"

print(swim_friends)

swim_friends["calvin"] = "doggystroke"

print(swim_friends)