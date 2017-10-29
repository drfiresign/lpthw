name = 'Dylan Cascio'
age = 30 # not a lie
height = 74 # inches
height_cm = height * 2.54 # centimeters
weight = 125 # lbs
weight_kg = round((weight * 0.453592), 2)
eyes = 'Blue'
teeth = 'Yellow'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches and {height_cm} centimeters tall.")
print(f"He's {weight} pounds and {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
