# import argv function from sys module
from sys import argv

#define the arguments passed in
script, filename = argv

# opening statement which declares what we're doing
# and how to stop it.
print """
We're going to erase %r.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
""" % filename

# prompt for user to accept truncation of file
raw_input("? ")

# open the file and assign it a variable name
print "Opening the file..."
target = open(filename, 'w')

# truncates the current file contents
print "Truncating the file. Goodbye!"
target.truncate()  # this is unecessary

# receive input lines
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# write out the lines of input to the file
print "I'm going to write these to the file."

total_line = "%s\n%s\n%s\n" % (line1, line2, line3)

target.write(total_line)

# close the file
print "And finally, we close it."
target.close()
