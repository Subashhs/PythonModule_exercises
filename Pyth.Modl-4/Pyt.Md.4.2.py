# Initialize a constant for the conversion factor from inches to centimeters
INCH_TO_CM = 2.54

while True:
    # Get user input for inches
    inches = float(input("Enter a length in inches (or a negative value to quit): "))

    # Check if the input is negative to end the program
    if inches < 0:
        print("Exiting the program.")
        break  # Exit the loop

    # Convert inches to centimeters and display the result
    centimeters = inches * INCH_TO_CM
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")
