# Try it Yourself | 6-11

cities = {
    'boston': {
        'country': 'USA',
        'population': 655000,
        'fact': 'Its the CCapital of Massachusetts'
    },

    'amsterdam': {
        'country': 'The Netherlands',
        'population': 814000,
        'fact': 'Its the Capital of Netherlands'
    },

    'moscow': {
        'country': 'Russia',
        'population': 2500000,
        'fact': 'Its the Capital of Russia'
    }
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    country = info['country']
    population = info['population']
    fact = info['fact']

    print(f"- Located in a country named {country.title()}")
    print(f"- Has an approx. population of {population}")
    print(f"- A little fact about {city.title()} is that {fact}")