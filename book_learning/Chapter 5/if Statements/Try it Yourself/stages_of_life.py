age = 67

if age < 2:
    message = "The individual is a baby."
elif age >= 2 and age < 4:
    message = "The individual is a toddler."
elif age >= 4 and age < 13:
    message = "The individual is a kid."
elif age >= 13 and age < 20:
    message = "The individual is a teenager."
elif age >= 20 and age < 65:
    message = "The individual is an adult."
else: 
    message = "The individual is an elder."

print(message)

# All age messages work
# Try it yourself 5-6