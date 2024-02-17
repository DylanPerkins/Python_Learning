file_path = "C:/Github/Python_Learning/book_learning/Chapter 10/Reading From a File/pi_million_digits.txt"

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))