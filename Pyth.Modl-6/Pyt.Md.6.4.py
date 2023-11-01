
min = int(input("Enter the minimum limit : "))
max = int(input("Enter the maximum range : "))
lst = list(range(min,max+1,1))

print(lst)
def sumlst():
    return sum(lst)

print(f" the sum of the integers in the list is {sumlst()}")