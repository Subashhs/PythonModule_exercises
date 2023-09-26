import random

# Get the number of random points from the user
num_points = int(input("Enter the number of random points to generate: "))

# Initialize a variable to count points inside the circle
points_inside_circle = 0

# Generate random points and check if they are inside the circle
for _ in range(num_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        points_inside_circle += 1

# Calculate the approximate value of pi
approx_pi = 4 * points_inside_circle / num_points

# Print the approximation of pi
print(f"Approximation of pi using {num_points} random points: {approx_pi}")
