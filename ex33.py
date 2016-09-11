def print_numbers_in_range(start, end, increment):
    numbers = []

    while start < end:
        print "At the top your number is %d" % start
        numbers.append(start)

        start += increment
        print "Numbers now: ", numbers
        print "At the bottom your number is %d" % start

    print "The numbers: "
    for num in numbers:
        print num


print_numbers_in_range(20, 300, 50)
