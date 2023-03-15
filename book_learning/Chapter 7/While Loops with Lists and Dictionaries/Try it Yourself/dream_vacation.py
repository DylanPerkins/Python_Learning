# Try it Yourself | 7-10

responses = []
flag = True

while flag:
    question = input(
        "If you could visit one place in the world, where would you go? ")

    responses.append(question)

    repeat = input("Do you have anywhere else you'd like to go? (yes/no) ")
    if repeat == 'no':
        flag = False

print("\n--- Polling Results ---")
for response in responses:
    print(f"- {response}")