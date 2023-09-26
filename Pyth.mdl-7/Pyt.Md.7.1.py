number_of_months = ("December", "January", "Febuary", "March", "April",
                    "May", "June", "July", "August", "September", "October",
                    "November" )
user = int(input("Write the number for the month: "))
seasons = "Winter", "Spring", "Summer", "Autum"
if user == (11, 0, 1):
    user = number_of_months
    print(f"{user} is {number_of_months}")

