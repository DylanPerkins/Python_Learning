people = ["mom", "dad", "cat"]
print(f"Hello {people[0].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[1].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[2].title()}, I was curious if you would like to come to dinner tonight!")

print(f"Sadly {people[1].title()} cannot make it to dinner tonight.")
people.remove("dad")
people.append("grandma")
print(f"Hello {people[0].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[1].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[2].title()}, I was curious if you would like to come to dinner tonight!")

