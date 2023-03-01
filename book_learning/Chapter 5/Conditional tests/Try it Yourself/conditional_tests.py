number = 57

print(" Is number >= 50? I predict True")
print(number >= 50)

print(" Is number >= 58? I predict False")
print(number >= 58)

print(" Is number <= 157? I predict True")
print(number <= 157)

print(" Is number >= 50 AND number >= 57? I predict True")
print(number >= 50 and number >= 57)

print(" Is number >= 58 or number <= 56? I predict False")
print(number >= 58 or number <= 56)

# 'Try it yourself' #5-1



car = 'audi'
print("Is car == 'subaru'? I predict False.")
print(car == 'subaru')

print("Is car == 'audi'? I predict True.")
print(car == 'audi')

car_1 = 'BMW'
print("Is car_1 equal to 'bmw'? I predict True")
print(car_1.lower() == 'bmw')

print("Is car_1 equal to 'subaru'? I predict false")
print(car_1.lower() == 'subaru')

supplies = ['paper', 'pen', 'pencil', 'backpack', 'eraser']
for supply in supplies:
    if supply == 'pen':
        print("We have a pen in our supplies!")

supply = 'laptop'
if supply not in supplies:
    print("We do not have our Laptop!")

# 'Try it yourself' #5-2
