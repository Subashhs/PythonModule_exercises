import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Seagates',
         autocommit=True
         )

area_code = input("Enter the are code to search airport: ")
sql = ("select name, type, municipality as location, ident from airport")
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if result:
    for name, type, location, ident in result:
        if area_code == ident:
            print(f"The airport {name} is {type} and the location is {location}. ")
    else:
        print("Invalid area code")

cursor.close()
connection.close()
