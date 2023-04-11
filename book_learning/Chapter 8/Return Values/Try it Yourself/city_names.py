# Try it Yourself 8-6

# Task: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted 
# like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.

def city_country(city, country):
    formatted = f"{city}, {country}"
    return formatted.title()

pair_1 = city_country("san salvador", "el salvador")
print(pair_1)

pair_2 = city_country("paris", "france")
print(pair_2)

pair_3 = city_country("rio de janeiro", "brazil")
print(pair_3)