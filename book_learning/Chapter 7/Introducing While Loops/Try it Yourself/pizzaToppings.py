# Try it Yourself | 7-5

prompt = "\nPlease enter what toppings you want on your pizza:"
prompt += "\n(When you're done, type 'quit'!) "

while True:
    message = input(prompt)

    if message == 'quit':
        print("We're going to start making your pizza now!")
        break
    else:
        print(f"We'll add {message} to your pizza!")