import mysql.connector
from geopy import distance
import random

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='Seagates',
    autocommit=True
)

def get_airport_info(icao):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT iso_country, ident, name, latitude_deg, longitude_deg FROM airport WHERE ident = %s;", (icao,))
    return cursor.fetchone()

def create_player():
    while True:
        name = input("Enter name: ")
        cursor = connection.cursor()
        cursor.execute(f"SELECT player_name FROM player WHERE player_name = '{name}'")
        if cursor.rowcount == 0:
            cursor.execute("INSERT INTO player(player_name,co2_budget,co2_consumed,total_travelled) VALUES (%s,%s,%s,%s)",
                           [name, 10000000, 0, 0])
            break
        else:
            print("Player already exists!")

    print(f"\nWelcome traveller, {name}!")
    return name

def show_and_choose_airplane(userid):
    cursor = connection.cursor()
    cursor.execute("SELECT type, size, capacity, co2_emission_per_km, max_range FROM airplane")
    results = cursor.fetchall()
    print("Please choose your airplane:")
    for idx, row in enumerate(results, start=1):
        print(f"{idx}. {row[0]}")
    choice = int(input("Your choice?(1-4): "))
    types = ['large_airport', 'medium_airport', 'heliport', 'small_airport']
    cursor.execute(f"UPDATE choice SET plane_type = '{types[choice-1]}' WHERE player_name = '{userid}'")
    return types[choice-1]

def calculate_distance(current, target):
    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km

def get_userdata(userid):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT player_name, co2_budget, co2_consumed, total_travelled FROM player WHERE player_name = %s", (userid,))
    return cursor.fetchone()

def left_budget(userid):
    data = get_userdata(userid)
    return data['co2_budget'] - data['co2_consumed']

def range_in(airplane_size, userid, turn, current='EFHK'):
    sql = f'''SELECT ident, airport.name, airport.continent, country.name as country, airplane.max_range, 
                    airplane.co2_emission_per_km, airplane.capacity
            FROM airport 
            INNER JOIN airplane ON (airplane.size = airport.type)
            INNER JOIN country ON (airport.iso_country = country.iso_country)
            WHERE airport.type = '{airplane_size}' ORDER BY RAND() LIMIT 5'''
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("\nHere are possible destinations you can choose:\n")
    print("num| continent | country | airport | distance | expected co2 emission")
    print("-----------------------------------------")
    destination = []
    for index, row in enumerate(result, start=1):
        airportCode = row[0]
        range_km = row[4]
        distance = calculate_distance(current, airportCode)
        co2_emission = distance * row[4] / row[5]
        if range_km > distance and co2_emission < left_budget(userid):
            destination.append((index, row[2], row[3], row[1], round(distance), round(co2_emission)))
            print(f"{index}  |  {row[2]}    | {row[3]} | {row[1]} | {round(distance)} km | {round(co2_emission)}")
    choice_input = input("\nWhere do you want to travel? Type the number or hit enter to change plane: ")
    if not choice_input:
        airplane = show_and_choose_airplane(userid)
        range_in(airplane, userid, turn)
        return
    choice = int(choice_input)
    if 1 <= choice <= len(destination):
        chosen = destination[choice - 1]
        chosenId, chosenDis, chosenCo2 = chosen[0], chosen[4], chosen[5]
        cursor.execute(f"UPDATE choice SET co2_spent = {chosenCo2}, distance_km = {chosenDis} WHERE turn = {turn} AND player_name = '{userid}'")

def event_occurrence(turn, userid):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM event")
    results = cursor.fetchall()
    weights, events = [], []
    for row in results:
        events.append(row[1])
        weights.append(row[3] * 100)
    pick = random.choices(events, weights=weights, k=1)[0]
    if pick != 'No event':
        print("\n\nYou've got a message from the control tower!")
        print(pick)
        if row[2] == 'neg':
            print(f"Co2 consumption is {row[4] * 100}% increased!")
            cursor.execute(f"UPDATE choice SET event_occurred = 1, co2_spent = co2_spent - co2_spent * {row[4]} WHERE turn = {turn} AND player_name = '{userid}'")
        elif row[2] == 'pos':
            print(f"Co2 consumption is {row[4] * 100}% decreased!")
            cursor.execute(f"UPDATE choice SET event_occurred = 1, co2_spent = co2_spent - co2_spent * {row[4]} WHERE turn = {turn} AND player_name = '{userid}'")

def update_turn_data(turn, userid):
    cursor = connection.cursor()
    cursor.execute(f"SELECT distance_km, co2_spent FROM choice WHERE turn = {turn} AND player_name = '{userid}'")
    result = cursor.fetchone()
    dis, co2 = result[0], result[1]
    cursor.execute(f"UPDATE player SET co2_consumed = co2_consumed + {co2}, total_travelled = total_travelled + {dis} WHERE player_name = '{userid}'")

def condition_checker(userid):
    cursor = connection.cursor()
    cursor.execute(f"SELECT co2_budget, co2_consumed FROM player WHERE player_name = '{userid}'")
    result = cursor.fetchone()
    co2_left = result[0] - result[1]
    if co2_left <= 0:
        return game_over_and_save(userid)

def game_over_and_save(userid):
    cursor = connection.cursor()
    cursor.execute(f"SELECT player_name, total_travelled FROM player WHERE (co2_budget <= co2_consumed) AND (player_name = '{userid}')")
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        print(f"{result[0]}, You cannot fly with the remaining budget anywhere. GAME OVER!")
        name, score = result[0], result[1]
        save = input("Do you want to save your score in")
