import random
import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='Seagates',
    autocommit=True
)
print("Welcome to Flight Game!!\n\n\n~ ~ ~ ~ ~~~~Flight Game~~~~~ ~ ~ ~ ~\n\n")

# Function to select airports for the game
def get_airport(icao):
    sql = "SELECT iso_country, airport, ident, name, type, Co2, latitude_deg, longitude_deg FROM airport WHERE ident = %s;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao))
    result = cursor.fetchone()
    return result



# Function to create a new player
def new_player():
    player_name = input("Enter your name: ")
    player_co2 = 50000

    cursor = connection.cursor()

    # Create the player table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS players
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       co2 INTEGER)''')

    # Insert the new player into the database
    cursor.execute("INSERT INTO players (name, Co2) VALUES (?, ?)", (player_name, player_co2))
    connection.commit()
    connection.close()
    print(f"Welcome, {player_name}! Your score is {player_co2}.\n")
    return player_name, player_co2


# Define a function to calculate CO2 consumption for a mission
def calculate_co2_distance(distance_km):
    return distance_km * 100  # Assuming 50 liters of CO2 for every 10 km

# Define a function to start the game
def start_game():
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}!")

    while True:
        print("\nOptions:")
        print("1. Start a mission")
        print("2. Settings")
        print("3. Information")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            mission_start = input("Enter the departure airport (ICAO code): ")
            mission_end = input("Enter the destination airport (ICAO code): ")

            player_co2 = 50000
            start_airport = get_airport(mission_start)
            end_airport = get_airport(mission_end)

            if start_airport and end_airport():
                distance = random.randint(10, 1000)  # Simulated random distance
                co2_consumed = calculate_co2_distance(distance)
                player_co2 += co2_consumed
                print(f"Mission completed! CO2 consumed: {co2_consumed} liters")
            else:
                print("Invalid airports. Try again.")

        if mission_start == "__main__":
            print("Welcome to the Flight Game!")
            start_game()

        elif choice == "2":
            print("Settings menu")

        elif choice == "3":
            print("Game information")

        elif choice == "4":
            print(f"Thank you, {player_name}!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    print("Welcome to the Flight Game!")
    start_game()
