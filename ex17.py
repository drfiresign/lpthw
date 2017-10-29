from sys import argv

script, from_file, to_file = argv
out_file = open(to_file, 'w').write(open(from_file).read())
