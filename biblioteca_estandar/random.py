import random

# Generated a random number int
random_number = random.randint(1, 100)
print(random_number)

# Ramdom colors
colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "black"]
color_random = random.choice(colors)
print(color_random)

#disorder
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(numbers)