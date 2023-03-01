people = ["mom", "dad", "luna"]
print(f"Hello {people[0].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[1].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[-1].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello everyone, I have actually found a bigger table so we can invite more guests!")

people.insert(0, "shane")
people.insert(2, "cody")
people.append("heidi")

print(f"Hello {people[0].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[1].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[2].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[3].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[4].title()}, I was curious if you would like to come to dinner tonight!")
print(f"Hello {people[5].title()}, I was curious if you would like to come to dinner tonight!")

print("Sorry everyone! The bigger table will not be available for our dinner session, so I will only be able to invite two guests, I will be sending those two another invite and informing the rest!")

revoked_invites = people.pop(0)
revoked_invites_2 = people.pop(0)
revoked_invites_3 = people.pop(0)
revoked_invites_4 = people.pop(0)
print(f"Hey {revoked_invites.title()}, sadly we won't be able to fit you at the table for dinner! I'm so sorry.")
print(f"Hey {revoked_invites.title()}, sadly we won't be able to fit you at the table for dinner! I'm so sorry.")
print(f"Hey {revoked_invites.title()}, sadly we won't be able to fit you at the table for dinner! I'm so sorry.")
print(f"Hey {revoked_invites.title()}, sadly we won't be able to fit you at the table for dinner! I'm so sorry.")

print(f"Great news {people[0].title()}! We are still on for dinner tonight!")
print(f"Great news {people[1].title()}! We are still on for dinner tonight!")

del people[0]
del people[0]

print(people)