# imports the argv method from the sys module
from sys import argv

# assigns the arguments passed in the CLi as usable arguments
script, filename = argv

# sets the file itself as a variable using the open() function
txt = open(filename)

# formats the file and uses the .read() function to actually read
# the contents of the file
print "Here's your file %r:" % filename
print txt.read()
txt.close()
