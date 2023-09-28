


from geopy.distance import geodesic
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Seagates',
         autocommit=True
         )

cursor = connection.cursor()
Icao_code1 = input("Enter First ICAO code of an airport : ")
Icao_code2 = input("Enter Second ICAO code of an airport : ")

cursor.execute("select latitude_deg, longitude_deg from ariport where ident = {icao_code1}"
airport1_cords = cursor.fetchone()
cursor.execute("select latitude_deg, longitude_deg from ariport where ident = {icao_code2}")
airport2_cords = cursor.fetchone()


    cursor.close()
    connection.close()
