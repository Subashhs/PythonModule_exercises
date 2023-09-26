#3 Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.
# Calculate the perimeter and area of the rectangle
#Get the length and with from the user
length = float(input("Enter thee length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

#Calculate the perimeter and area of the rectangleeee
perimeter = 2 * (length + width)
area = length * width

#Print the results
print(f"The perimeter of the rectangle is {perimeter: .2f}")
print(f"The area of the rectangle is {area: .2f}")
