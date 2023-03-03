# Section: A List of Dictionaries

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens
for alien_number in range(30): # Returns a series of numbers that we want to loop through
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien) # Adds each new alien to the list `aliens`

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}") # Prints the length of the list `aliens`
