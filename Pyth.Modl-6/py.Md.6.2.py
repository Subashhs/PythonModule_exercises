import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    max_number = int(input("Enter the maximum number on the dice: "))
    while True:
        result = roll_dice(max_number)
        print("Dice roll result:", result)
        if result == max_number:
            break

if __name__ == "__main__":
    main()
