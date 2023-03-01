my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# Use of [:] creates a slice of the entire list

my_foods.append('cannoli')
friend_foods.append('ice cream')
# If you set the lists equal to each other, both items would appear in both lists. However, our method of using [:] makes both lists unique.

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)