import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Seagates',
         autocommit=True
         )
Icao_code = input("Enter ICAO code of an airport : ")
sql = ("select name, municipality as location, ident from airport")
cursor = connection.cursor()
cursor.execute(sql)
results = cursor.fetchall()
if results:
        for name, location, ident in results:
            if Icao_code == ident:
                print((f"The airport is {name} and the location is {location}"))
else:
    print("ICAO code not matched")

    cursor.close()
    connection.close()
