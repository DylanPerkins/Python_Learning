# Try it Yourself | 6-10

favorite_numbers = {
    'joe': [29, 37, 20], 
    'mike': [60, 47, 1],
    'leo': [18, 87, 90],
    'ben': [33, 11, 22],
    'abe': [7, 67, 3]
}

for name, favorite_number in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are: ")
    for number in favorite_number:
        print(f"\t{number}")