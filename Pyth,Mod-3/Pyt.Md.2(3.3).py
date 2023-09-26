user = input("What is the biological gender? (f or m) : ")
Hemg = float(input("What is the hemoglobin value (g/l)? : "))
Male = 'm'
Female = 'f'
if(user == 'f'):
    if (Hemg < 117):
        print("Hemoglobin value is low.")
    elif(Hemg >= 117 and Hemg <= 155):
        print("Its normal for adult Female.")
    elif(Hemg > 155 ):
     print("Hemoglobin value is high.")

if(user == 'm'):
    if (Hemg < 134):
        print("Hemoglobin value is low.")
    elif(Hemg >= 134 and Hemg <= 167):
        print("Its normal for adult Male.")
    elif(Hemg > 167 ):
     print("Hemoglobin value is high.")
    

else:
    print("Invalid Input.")

