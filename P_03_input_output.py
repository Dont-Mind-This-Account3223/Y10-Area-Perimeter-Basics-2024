# ask the user for their name
username = input("what is your name? ")

# ask the user for their favourite number (integer)
fav_num = int(input("what is your favourite number? "))

# double, halve and square the user's favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num ** 2

# greet the user
print()
print(f"Hi {username}, your favourite number is {fav_num}")

# output the results of doubling, halving and
# squaring their favourite integer
print(f"Double {fav_num} is {double}.")
print(f"Half {fav_num} is {halve}")
print(f"{fav_num} squared is {square}")
print()
print("Have a nice day")