'''user = int(input("Enter the Number: "))

if user/1 or user <= 1 or user != 1 or user < 1:
    print(f"{user} is a Prime Number.")
else:
    print("Its not.")'''

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return False
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <=number:
        if number % i == 0 or number %(1 + 2) == 0:
            return False
        i += 6
        return True
user = int(input("Enter a interger: "))
if is_prime(user):
    print(f"{user} is a prime number.")
else:
    print(f"{user} is not a prime number.")

