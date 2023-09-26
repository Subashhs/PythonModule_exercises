# Initialize empty lists to store the entered numbers
numbers = []

# Loop to get input from the user until they enter an empty string
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the input is an empty string to exit the loop
    if user_input == "":
        break

    try:
        # Convert the user input to a float and append it to the list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if any numbers were entered
if numbers:
    # Find the smallest and largest numbers
    smallest = min(numbers)
    largest = max(numbers)

    # Print the results
    print(f"Smallest number entered: {smallest}")
    print(f"Largest number entered: {largest}")
else:
    print("No numbers were entered.")
