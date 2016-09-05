# data format
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# 2 string format interpolations
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r forces the "return result" (if you will) of a variable
print "I said: %r." % x
# %s only replaces the string version of a variable
print "I also said: '%s'." % y

# you can also use format like an operational sign
hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# you can add strings
w = "This is the left side of..."
e = "a string with a right side."

print w + e

# 1 Go through this program and write a comment above each line explaining it.
# done
# 2 Find all the places where a string is put inside a string. There are four places.
# Yes, there are 4
# 3 Are you sure there are only four places? How do you know? Maybe I like lying.
# Nope, the others are using the %r format to put out only the store data, with no conversion
# 4 Explain why adding the two strings w and e with + makes a longer string.
# because they're contateonated.
