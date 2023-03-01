alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) 
# Doesnt exist!

# If you attempt to make a call to a key that isnt in the selected 
# dictionary then it will return with a KeyError


alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

# We can use the `get` function to set a default value for a key. 
# If you attempt to call a key from a dictionary that does not 
# exist and you have this function in place, it will throw that
# default value that you've just set.

# If you do have that key in your dictionary, then it will instead 
# pull that key's value directly.

# If you leave out the second argument in the call to get() 
# and the key doesnt exist, Python will return the value None. 
# The special value `None` means “no value exists.”
# This is not an error: its a special value meant to indicate the 
# absence of a value. 