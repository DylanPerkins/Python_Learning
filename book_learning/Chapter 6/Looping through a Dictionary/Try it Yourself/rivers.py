# Try it Yourself | 6-5

rivers = {
    'mediterranean': 'nile',
    'atlantic ocean': 'amazon',
    'east china sea': 'yangtze'
}

for location, name in rivers.items():
    print(f"The {name.title()} is located in the {location.title()}.")

for name in rivers.values():
    print(f"{name.title()}")

for location in rivers.keys():
    print(f"{location.title()}")