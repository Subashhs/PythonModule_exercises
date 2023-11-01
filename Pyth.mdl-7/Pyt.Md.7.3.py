# Initialize an empty dictionary to store airport data
airport_data = {}


# Function to add a new airport to the dictionary
def add_airport():
    icao_code = input("Enter the ICAO code of the airport: ")
    airport_name = input("Enter the name of the airport: ")
    airport_data[icao_code] = airport_name
    print(f"Airport {icao_code} - {airport_name} added successfully.")


# Function to fetch airport information
def fetch_airport():
    icao_code = input("Enter the ICAO code of the airport: ")
    if icao_code in airport_data:
        print(f"The name of the airport with ICAO code {icao_code} is: {airport_data[icao_code]}")
    else:
        print(f"Airport with ICAO code {icao_code} not found in the database.")


# Main program loop
while True:
    print("\nAirport Data Management System")
    print("1. Add a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_airport()
    elif choice == '2':
        fetch_airport()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
