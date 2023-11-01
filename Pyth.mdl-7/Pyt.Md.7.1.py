months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
seasons = ("spring", "summer", "autumn", "winter")


number_of_month = int(input("Enter the number of month: "))
month = months[number_of_month-1]

print(f" The {number_of_month} the month is {month}")

def season(month):
    if month in months[2:5]:
        print(f" It is {seasons[0]} season.")
    elif month in months[5:8]:
        print(f" It is {seasons[1]} season.")
    elif month in months[8:11]:
        print(f" It is {seasons[2]} season.")
    else:
        print(f" It is {seasons[-1]} season.")

    return
season(month)