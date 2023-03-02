# Looping Through All Key-Value Pairs

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items(): # Returns a list of key-value pairs
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# This code will assign the keys within the dictionary to the 
# variable 'key', and the key's values will be assigned to the 
# variable 'value'. We can then print them out