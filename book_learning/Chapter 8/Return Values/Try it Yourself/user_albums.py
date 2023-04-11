# Try it Yourself 8-8

# Task:
# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title):
    formatted_album = {'Artist Name': artist_name.title(), 'Album Title': album_title.title()}
    return formatted_album

while True:
    print("\nLet's log your favorite album!")
    print("Note: Enter 'q' to exit this menu!")
    album_name = input("What is the name of the album: ")
    if album_name == 'q':
        break

    artist_name = input("Who wrote that album: ")
    if artist_name == 'q':
        break

    formatted_info = make_album(artist_name, album_name)
    print(formatted_info)
