# Try it Yourself | 7-5

prompt = "How old are you? "
ticketPrice = 0
age = int(input(prompt))

if age > 12:
    ticketPrice = 15
elif age > 3 & age < 12:
    ticketPrice = 10
else:
    ticketPrice = 0

print(f"The price of your ticket is ${ticketPrice}.")