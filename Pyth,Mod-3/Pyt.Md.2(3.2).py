user = input("Enter the cabin class of cruise ship. Option(LUX,A,B,C): ")

if(user == 'LUX'):
    print("Upper deck cabin with a balcony.")
elif(user == 'A'):
    print("Above the car deck, equipped with a window.")
elif(user == 'B'):
    print("Windowless cabin above the car deck.")
elif(user == 'C'):
    print("Windowless cabin below the car deck.")

else:
    print("Invalid Cabin Class.")

