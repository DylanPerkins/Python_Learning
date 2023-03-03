# Try it Yourself | 6-9

favorite_places = {
    'dylan': ['bedroom', 'school', 'bike trail'],
    'heidi': ['resturants', 'movie theater', 'school'],
    'luna': ['litter box', 'bed', 'boxes']
}

for name, locations in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for location in locations:
       print(f"\t{location.title()}")