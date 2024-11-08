prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]


squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(squares)


# start, end, and step

# start: where you start the list (default = 0)

# end: where you end (but actually it ends before the end)

# step: difference between consecutive numbers (default = 1)

# 1 parameter: just the end value

# 2 parameters: start and end in thaat order

# 3 parameters: start, end, step in that order

range(8) # 0, 1, 2, 3, 4, 5, 6, 7

range(2, 5) # 2, 3, 4

range(5, 10, 2) # 5, 7, 9

range(6) # 0, 1, 2, 3, 4, 5

range(1) # 0 

range(10, 14) # 10 , 11, 12, 13

range(3, 15, 3) # 3, 6, 9, 12

range(2, 14, 7)# 2, 9

for number in range(1, 11):
    print(number * number)

numbers = list(range(1, 11))

print(numbers)

value = 15

if value < 1:
    print(value)
elif value > 5:
    print("big")
else: 
    print("positive")

value = 15

if value != 15 or value > 5:
    print("both")