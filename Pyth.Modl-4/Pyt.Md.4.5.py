# Define the correct username and password
correct_username = "python"
correct_password = "rules"

# Initialize the number of login attempts
attempts = 0

# Loop for login attempts
while attempts < 5:
    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password are correct
    if username == correct_username and password == correct_password:
        print("Welcome")
        break  # Exit the loop if login is successful
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1

# Check if the user failed to login after five attempts
if attempts == 5:
    print("Access denied. You have reached the maximum number of login attempts.")
