
R1 = (int(input("Diameter 1: "))/2)/100
P1 = int(input("Price 1: "))

R2 = (int(input("Diameter 2: "))/2)/100
P2 = int(input("Price 2: "))
def unitprice(radius, price):
    return (f"-The unit price is: {(price/(3.14 * (float(radius))**2))}")



first_rate = unitprice(R1 , P1)
print(f" {first_rate} per sq m for the first pizza.")
second_rate = unitprice(R2 , P2)
print(f" {second_rate} per sq m for the second pizza.")

if first_rate < second_rate:
    print(f"Go with the first one. Tt is better value for money. ")
elif first_rate == second_rate:
    print("~~~~Both are equally valued.~~~~")
else:
    print("Second one is better value for money.")
