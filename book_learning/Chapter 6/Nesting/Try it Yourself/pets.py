# Try it Yourself | 6-8

pet_0 = {
    'type': 'dog',
    'owner': 'john'
}

pet_1 = {
    'type': 'cat',
    'owner': 'dylan'
}

pet_2 = {
    'type': 'mouse',
    'owner': 'beth'
}

pet_3 = {
    'type': 'hamster',
    'owner': 'heidi'
}

pet_4 = {
    'type': 'ferret',
    'owner': 'casey'
}

pet_5 = {
    'type': 'snake',
    'owner': 'michelle'
}

pets = [pet_0, pet_1, pet_2, pet_3, pet_4, pet_5]
counter = 0

for pet in pets:
    for keys, answer in pet.items():
        print(f"{keys.title()}: {answer.title()}")
        counter = counter + 1
    if (counter == 2):
        counter = 0
        print("")
