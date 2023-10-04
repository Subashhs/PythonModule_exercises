import random

from geopy import distance

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
def get_airport():
    sql = ("select iso_country, airoprt, ident, name type, latitude_deg, longitude_deg from airport;")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


#get goals
def get_goals():
    sql = "select * from goal;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#new game
def new_game(default_Co2, ):







connection.close()

