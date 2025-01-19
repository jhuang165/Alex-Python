# guessing game part 2

low = 1
high = 100

while low <= high:
    guess = (low + high - (low + high) % 2) / 2 
    answer = input(f"Is your number {guess}? (Answer Y if correct, H if too high, and L if too low.) ")
    if answer == "Y":
        print("Yay!")
        break
    elif answer == "H":
        high = guess - 1
    elif answer == "L":
        low = guess + 1
    else:
        print("Sorry I don't recognize that answer. Try again!")
        continue
