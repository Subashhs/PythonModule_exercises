
start = int(input("Enter Minimum: "))
End = int(input ("Enter Maximum: "))

full_list = list(range(start, End+1, 1))
print(f"-The complete list is {full_list}")

even = []
for i in full_list:
    if i%2 == 0:
        even.append(i)
print(f"-The list of even numbers is {even}")