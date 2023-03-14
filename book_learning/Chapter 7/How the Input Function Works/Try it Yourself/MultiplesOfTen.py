# Try it Yourself | 7-3

number = input("Give me a number, and I will tell you if it's a multiple of 10!: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is indeed a multiple of 10, very nice!")
else:
    print(f"Unfortunately {number} is not a multiple of 10.")