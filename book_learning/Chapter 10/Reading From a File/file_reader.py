file_path = "C:/Github/Python_Learning/book_learning/Chapter 10/Reading From a File/pi_digits.txt"

with open(file_path) as file_object:
    contents = file_object.read()

print(contents.rstrip())  # Prints file content but removes whitespace
print("\n")

### Notes:

# The open() function is used to open and access a file's contents. It then
# returns an object representing the file. Next we assign this object to the
# variable `file_object`, kinda of like an alias in terms of syntax and usage.

# The keyword `with`, that we use at the start of the program, closes the file
# access once it is no longer needed. You can also explicitly close the file with
# the `close()` function, but if an error occurs that prevents the close function
# from being reached or executed, then the file wouldn't close. Which can lead
# to data loss or corruption.

# Next, we call the read() function on the file object and set the output of the
# function to a new variable named contents. The read() function reads the
# entire contents of the file and then stores it as one long string.


### Section: Reading Line by Line

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n")


### Section: Making a List of Lines from a File

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
