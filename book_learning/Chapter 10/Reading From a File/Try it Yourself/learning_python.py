### Try it Yourself: 10-1

### Task:
# Open a blank file in your text editor and write a few
# lines summarizing what you've learned about Python so far. Start each line
# with the phrase In Python you can... . Save the file as learning_python.txt in
# the same directory as your exercises from this chapter. Write a program that
# reads the file and prints what you wrote three times. Print the contents once by
# reading in the entire file, once by looping over the file object, and once by
# storing the lines in a list and then working with them outside the with block.

file_path = "C:/Github/Python_Learning/book_learning/Chapter 10/Reading From a File/Try it Yourself/learning_python.txt"

# Method 1
with open(file_path) as file_object:
    contents = file_object.read()

print(contents.rstrip())
print("\n")

# Method 2
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n")

# Method 3
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

### Try it Yourself: 10-2

### Task:
# You can use the replace() method to replace any word in a
# string with a different word. Read in each line from the file you just
# created, learning_python.txt, and replace the word Python with the name of
# another language, such as C. Print each modified line to the screen

print("\n")

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace("Python", "Java"))
