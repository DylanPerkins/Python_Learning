# Try it Yourself 8-7

# Task:
# Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title, num_of_songs=None):
    formatted_album = {'Artist Name': artist_name.title(), 'Album Title': album_title.title()}
    if num_of_songs:
        formatted_album['Number of Songs in Album'] = num_of_songs
    return formatted_album

album_1 = make_album("justin bieber", "believe")
print(album_1)

album_2 = make_album("demi lovato", "here we go again")
print(album_2)

album_3 = make_album("21 savage", "savage mode")
print(album_3)

album_4 = make_album("harry styles", "fine line", 12)
print(album_4)