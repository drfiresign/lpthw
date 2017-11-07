def print_numbers(b, e):
    i = b
    numbers = []
    while i < e:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    for num in numbers:
        print(num)

print_numbers(30, 32)
print_numbers(45, 50)
print_numbers(2, 20)
