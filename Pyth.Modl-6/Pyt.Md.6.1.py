import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        result = roll_dice()
        print("Dice roll result:", result)
        if result == 6:
            break

if __name__ == "__main__":
    main()
