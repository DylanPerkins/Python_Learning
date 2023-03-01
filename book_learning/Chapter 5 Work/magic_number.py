answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
# If the user input does not equal 42, print this message


#Bi-conditional statment
print(answer < 21)
# Is the value of answer less than 21? 

print(answer <= 21)
# Is the value of answer less than or equal to 21? 

print(answer > 21)
# Is the value of answer greater than 21? 

print(answer >= 21)
# Is the value of answer greater than or equal to 21? 



age_0 = 22
age_1 = 18
print((age_0 >= 21) and (age_1 >= 21))
# Checks if age_0 is greater than or equal to 21 AND if age_1 is...
# ...greater than or equal to 21. If either is false, the...
# statement is false.

age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))
# Same as last, but with a different value for age_1.


age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >= 21))
# Checks if age_0 is greater than or equal to 21 OR if age_1 is...
# ...greater than or equal to 21. If either is true, the...
# statement is true.

age_0 = 18
print((age_0 >= 21) or (age_1 >= 21))
# Same as last, but with a different value for age_0.