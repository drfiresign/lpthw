# import argument variables
from sys import argv

script, filename = argv

# basic explantory text
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# opening the file in write mode (with the w)
target = open(filename, 'w')

# truncate, or delete (collapse?) whatever data was previously there
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

# taking in three separate lines as variable, one at a time
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# writing one variable, then a new line char, another var, etc.
# to the target file variable
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
