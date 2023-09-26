import random

num_roll = int(input("How many dice to roll: "))

total_roll = 0

for _ in range(num_roll):

    roll = random.randint(1, 6)

    total_roll += roll

print(f"The sum of the {num_roll} is the {total_roll} :")
