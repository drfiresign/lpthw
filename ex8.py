# defines the formatter variable using the traditional {} notation
formatter = "{} {} {} {}"

# formats using numbers
print(formatter.format(1, 2, 3, 4))
# formats using strings of numbers
print(formatter.format("one", "two", "three", "four"))
# formats using boolean expressions
print(formatter.format(True, False, False, True))
# formats using the same formatter variable turning each instance
# of the {} notation into a string with "{} {} {} {}"
print(formatter.format(formatter, formatter, formatter, formatter))
# formats a multi line argument into a single line.
# the comma , allows for the multi line structure
print(formatter.format(
	"here's a short poem",
	"it's about the length",
	"of most poems",
	"i've ever written."
))
