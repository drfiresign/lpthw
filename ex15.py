# import argv to use
from sys import argv

# assign argument variables including filename to be parsed
script, filename = argv

# open the passed in filename
txt = open(filename)

print(f"Here's your file {filename}:")
# read and print the file contents to stdout
print(txt.read())

#print("Type the filename again:")
## get another or the same file to print
#file_again = input("> ")
#
#txt_again = open(file_again)
#
## print out that file again
#print(txt_again.read())
txt.close()
#txt_again.close()
