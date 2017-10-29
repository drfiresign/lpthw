from sys import argv

script, first = argv

print("The title of this script is:", script)
print("The first color you chose was:", first)

street = input("What street did you grow up on? ")
age = input("How old are you? ")

print(f"Your Livejournal name is xXx{first}{age}{street}xXx")
