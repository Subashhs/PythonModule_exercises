names = set()
name = input("Enter the name: ")

while name != "":
    if name in names:
        names.add(name)
        print("Existing name.")
    else:
        names.add(name)
        print("New name.")
    name = input("Enter the name:")

for i in names:
    print(i)