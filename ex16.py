# import argument variables
from sys import argv

script, filename = argv

print("Opening the file...")
# opening the file in write mode (with the w)
target = open(filename, 'w')
# truncation isn't necessary when using the w option

print("Now I'm going to ask you for three lines.")

# taking in three separate lines as variable, one at a time
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
nl = "\n"

print("I'm going to write these to the file.")

# writing one variable, then a new line char, another var, etc.
# to the target file variable
final_write = line1 + nl + line2 + nl + line3 + nl
target.write(final_write)

print("And finally, we close it.")
target.close()
