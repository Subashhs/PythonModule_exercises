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
print("Welcome to Flight Game!!\n~~~~~Flight Game~~~~~\n1.Start Game")

# Function to select airports for the game
def get_airport(icao):
    sql = "SELECT iso_country, airport, ident, name, type, latitude_deg, longitude_deg FROM airport WHERE ident = %s;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao))
    result = cursor.fetchone()
    return result

# Get goals
def get_goals():
    sql = "SELECT * FROM goal;"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# Create a new game
def new_game(default_Co2, ply_range, curnt_airport, pre_airport, a_irports):
    sql = "INSERT INTO game (Co2, player_range, location, screen_name) VALUES (%s, %s, %s, %s);"
    cursor = connection.cursor()
    cursor.execute(sql, (default_Co2, ply_range, curnt_airport, pre_airport))
    game_id = cursor.lastrowid

    # Add goals
    goals = get_goals()
    goals_list = []
    for goal in goals:
        for i in range(0, goal['maybe'], 1):
            goals_list.append(goal['id'])

    # Exclude starting airport
    game_airports = a_irports[1:].copy()
    random.shuffle(game_airports)

    for i, goal_id in enumerate(goals_list):
        sql = "INSERT INTO ports (game, airport, goal) VALUES (%s, %s, %s);"
        cursor = connection.cursor()
        cursor.execute(sql, (game_id, game_airports[i]['ident'], goal_id))

    return game_id

# Check goals for airport
def check_goal(game_id, curnt_airport):
    sql = "SELECT ports.id, goal, goal.id AS goal_id, name, Co2 FROM ports JOIN goal ON goal.id = ports.goal WHERE game = %s AND airport = %s;"
    cursor = connection.cursor()
    cursor.execute(sql, (game_id, curnt_airport))
    result = cursor.fetchone()
    if result is None:
        return False
    return result

# Calculate distance between two airports
def calculate_distance(current, target):
    start = get_airport(current)
    end = get_airport(target)
    start_coords = (start['latitude_deg'], start['longitude_deg'])
    end_coords = (end['latitude_deg'], end['longitude_deg'])
    return distance.distance(start_coords, end_coords).km

# Get airports in range
def airports_in_range(icao, a_irports, ply_range):
    in_range = []
    for airport in a_irports:
        dist = calculate_distance(icao, airport['ident'])
        if 0 < dist <= ply_range:
            in_range.append(airport)
    return in_range

# Update location
def update_location(icao, ply_range, U_Co2, game_id):
    sql = "UPDATE game SET location = %s, player_range = %s, Co2 = %s WHERE id = %s;"
    cursor = connection.cursor()
    cursor.execute(sql, (icao, ply_range, U_Co2, game_id))

# Main game loop
if __name__ == "__main__":
    current_airport = 'curnt_airport'  # Replace with your starting airport
    Co2 = 2000
    player_range = 3000
    player = input("Player's name: ")
    all_airports = get_airport(current_airport)

    game_id = new_game(Co2, player_range, current_airport, player, all_airports)

    game_over = False
    win = False

    while not game_over:
        airport = get_airport(current_airport)
        print(f"You are at {airport['name']}.")
        print(f"You have {Co2:.0f} ltr and {player_range:.0f} km of range.")

        input('\033[32mPress Enter to continue...\033[0m')

        goal = check_goal(game_id, current_airport)
        if goal:
            question = input(
                f"Do you want to open reward for {'100 ltr or ' if Co2 > 100 else ''}{'50 km range' if player_range > 50 else ''}? C = Co2, R = range, enter to skip: ")
            if not question == '':
                if question == 'C':
                    Co2 -= 100
                elif question == 'R':
                    player_range -= 50
                if goal['Co2'] > 0:
                    Co2 += goal['Co2']
                    print(f"Congratulations! You found {goal['name']}. That is worth {goal['Co2']} ltr.")
                    print(f"You have now {Co2:.0f} ltr.")
                elif goal['Co2'] == 0:
                    win = True
                    print("Congratulations! You have completed the mission. Now go to the start.")
                else:
                    money = 0
                    print("Mission Failed. You lost all your Co2")

        input("\033[32mPress Enter to continue...\033[0m")

        if Co2 > 0:
            question2 = input('Do you want to buy Co2? 5 ltr = 10 km of range. Enter amount or press enter: ')
            if not question2 == '':
                question2 = float(question2)
                if question2 > Co2:
                    print("You don't have enough money.")
                else:
                    player_range += question2 * 10
                    Co2 -= question2
                    print(f"You have now {Co2:.0f} ltr and {player_range:.0f} km of range.")

        airports = airports_in_range(current_airport, all_airports, player_range)
        print(f"\033[34mThere are {len(airports)} airports in range: \033[0m")

        if len(airports) == 0:
            print('You are out of range.')
            game_over = True
        else:
            print(f"Airports: ")
            for airport in airports:
                ap_distance = calculate_distance(current_airport, airport['ident'])
                print(f"{airport['name']}, icao: {airport['ident']}, distance: {ap_distance:.0f} km")

            dest = input('Enter destination ICAO code: ')
            selected_distance = calculate_distance(current_airport, dest)
            player_range -= selected_distance
            update_location(dest, player_range, Co2, game_id)
            current_airport = dest

            if player_range < 0:
                game_over = True

        if win and current_airport == 'InitialAirport':
            print(f"You won! You have {Co2} ltr and {player_range} km of range left.")
            game_over = True

    print(f"{'You won!' if win else 'You lost!'}")
    print(f"You have {Co2:.0f} ltr")
    print(f"Your range is {player_range:.0f} km")