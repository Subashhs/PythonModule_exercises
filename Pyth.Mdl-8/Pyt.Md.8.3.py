
from geopy.distance import geodesic
import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='Seagates',
         autocommit=True
         )


airport1_icao = input("Enter First ICAO code of an airport : ")
airport2_icao = input("Enter Second ICAO code of an airport : ")
cursor = connection.cursor()
sql1 = (f"select latitude_deg, longitude_deg from ariport  where ident = '{airport1_icao}'")
cursor.execute(sql1)
airport1_cords = cursor.fetchone()
sql2 = (f"select latitude_deg, longitude_deg from ariport where ident = '{airport2_icao}'")
cursor.execute(sql2)

airport2_cords = cursor.fetchone()

if airport1_cords is None or airport2_cords is None:
    print("One or both airport not found in the database.")
else:
    lat1, lon1 = airport1_cords
    lat2, lon2 = airport2_cords

    airport1 = (lat1, lon1)
    airport2 = (lat2, lon2)
    distance_km = geodesic(airport1, airport2).kilometers

    print(f"The distance between two airport is approximately {distance_km:.2f} kilometers.")



cursor.close()
connection.close()
