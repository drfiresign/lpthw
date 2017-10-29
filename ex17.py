from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these on one line, how?
indata = open(from_file).read()

print(f"The input file is {len(indata)} byes long")

if exists(to_file):
    continue
else:
    print("To file not found.")
    break

out_file = open(to_file, 'w')
out_file.write(indata)

print("All done. Bye bye.")

out_file.close()
in_file.close()
