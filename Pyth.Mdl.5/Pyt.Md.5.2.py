'''numbers = []

user = input("Input the number or press enter to quit: ")
while user != "":
    numbers.append(user)
    input("Input the number or press enter to quit: ")

'''
# Initialize an empty list to store numbers
numbers = []

# Take user input until an empty string is entered
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the user wants to quit (empty input)
    if user_input == "":
        break

    try:
        # Try to convert the user input to a float and add it to the list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if there are at least five numbers entered
if len(numbers) >= 5:
    # Sort the numbers in descending order
    numbers.sort(reverse=True)

    # Print the top five numbers
    print("The five greatest numbers sorted in descending order are:")
    for i in range(5):
        print(numbers[i])
else:
    print("You need to enter at least five numbers to find the top five.")




