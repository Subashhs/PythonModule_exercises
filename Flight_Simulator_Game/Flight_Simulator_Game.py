import random

import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='Seagates',
         autocommit=True
         )


#Function
#select airports for tha game
def get_airport(icao):
    sql = ("select iso_country, airoprt, ident, name, type, latitude_deg, longitude_deg from airport where ident = %s;")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


#get goals
def get_goals():
    sql = "select * from goal;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#new game
def new_game(default_Co2, ply_range, curnt_airport, pre_airport, a_irports):
    sql = "Insert into game (Co2, player_range, location, screen_name) values (%s, %s, %s, %s);"
    cursor = connection.cursor()
    cursor.excute(sql(default_Co2, ply_range, curnt_airport, pre_airport, a_irports))
    game_id = cursor.last

    #add goals
    goals = get_goals()
    goals_list = []
    for goal in goals:
        for i in range(0, goal['maybe'], 1):
            goals_list.append(goal['id'])

    #excluding starting airport
    game_airport = a_irports[1:].copy()
    random.shuffle(game_airport)

    for i, goal_id in enumerate(goals_list):
        sql = "Insert into ports(game, airport, gpal) values (%s, %s, %s);"
        cursor = connection.cursor()
        cursor.execute(sql, (game_id, game_airport[i]['ident'], goal_id))

    return game_id

#check goals for airport
def check_goal(game_id, curnt_airport):
    sql = (f"select ports.id, goal, goal.id as goal_id, name, Co2 from ports join goalon goal.id = ports.goal where game = %s and airport = %s")
    cursor = connection.cursor()
    cursor.excute(sql, (game_id , curnt_airport))
    result = cursor.fetchone()
    if result is None:
        return False
    return result

#calculate distance between two airports
def calculate_distance(current, target):
    from geopy import distance
    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance(start['latitude_deg'], start['longitude_deg']),
    (end['latitude_deg'], end['longitude_deg']).km

#get airports in range
def airports_in_range(icao, a_irports, ply_range):
    in_range = []
    for a_irport in a_irports:
        dist = calculate_distance(icao, a_irport['ident'])
        if dist <= ply_range and not dist == 0:
            in_range.append(a_irport)
    return in_range

#update location
def update_location(icao, ply_range, U_Co2, game_id):
    sql = f"update game set location = %s, player_range = %s, Co2 = %s where id %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao, ply_range, U_Co2, game_id))

    #game starts
    gamestart = input("Do you want to start the game? (Y/N): ")
    if gamestart == 'Y':
        for line in game.start():
            print(line)


    #Game settings
    print("Start Game")
    player = input("Players name: ")
    game_over = False
    win = False

    #Starting Co2 with player in liters
    Co2 = 2000
    player_range = 3000

    #score
    score = 0

    #all airports
    all_airports = get_airport()

    #beginning ident airport
    start_airport = start_airport

    #game id
    game_id = create_game(Co2, player_range, start_airport, player, all_airports)

    #Loop in game
    while not game_over:
        # get current airport info
        airport = get_airport_info(current_airport)
        # show game status
        print(f"You are at {airport['name']}.")
        print(f"You have {Co2:.0f}ltr and {player_range:.0f}km of range.")
        # pause
        input('\033[32mPress Enter to continue...\033[0m')
        # if airport has goal ask if player wants to open it
        # check goal type and add/subtract money accordingly
        goal = check_goal(game_id, current_airport)
        if goal:
            question = input(
                f'''Do you want to open reward for {"100 ltr or " if Co2 > 100 else ""}{"50km range" if player_range > 50 else ""}? C = Co2, R = range, enter to skip: ''')
            if not question == '':
                if question == 'M':
                    Co2 -= 100
                elif question == 'R':
                    player_range -= 50
                if goal['Co2'] > 0:
                    Co2 += goal['Co2']
                    print(f'''Congratulations! You found {goal['name']}. That is worth {goal['Co2']}ltr.''')
                    print(f'''You have now {Co2:.0f}$''')
                elif goal['Co2'] == 0:
                    win = True
                    print(f'''Congratulations! You have completed mission. Now go to start.''')
                else:
                    money = 0
                    print(f"Mission Failed. You lost all your Co2")

        # pause
        input("\033[32mPress Enter to continue...\033[0m")

        # ask to buy fuel/range
        if Co2 > 0:
            question2 = input('Do you want to buy Co2? 5ltr = 10km of range. Enter amount or press enter. ')
            if not question2 == '':
                question2 = float(question2)
                if question2 > Co2:
                    print(f"You don't have enough money.")
                else:
                    player_range += question2 * 2
                    Co2 -= question2
                    print(f"You have now {Co2:.0f}ltr and {player_range:.0f}km of range.")
            # pause
            input("\033[32mPress Enter to continue...\033[0m")

        # if no range, game over
        # show airports in range. if none, game over
        airports = airports_in_range(current_airport, all_airports, player_range)
        print(f"\033[34mThere are {len(airports)} airports in range: \033[0m")
        if len(airports) == 0:
            print('You are out of range.')
            game_over = True
        else:
            print(f"Airports: ")
            for airport in airports:
                ap_distance = calculate_distance(current_airport, airport['ident'])
                print(f"{airport['name']}, icao: {airport['ident']}, distance: {ap_distance:.0f}km")
            # ask for destination
            dest = input('Enter destination icao code: ')
            selected_distance = calculate_distance(current_airport, dest)
            player_range -= selected_distance
            update_location(dest, player_range, Co2, game_id)
            current_airport = dest
            if player_range < 0:
                game_over = True
        # if diamond is found and player is at start, game is won
        if win and current_airport == start_airport:
            print(f"You won! You have {Co2}ltr and {player_range}km of range left.")
            game_over = True

    # if game is over loop stops
    # show game result
    print(f"{'You won!' if win else 'You lost!'}")
    print(f"You have {Co2:.0f}ltr")
    print(f"Your range is {player_range:.0f}km")















