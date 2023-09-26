#Write a program that asks the user to enter a mass in medieval units: talents
# (leiviskä), pounds (naula), and lots (luoti). The program converts the input to f
# ull kilograms and grams and outputs the result to the user:

#One talent is 20 pounds.
#One pound is 32 lots.
#One lot is 13,3 grams.

# Get the mass in medieval units from the userrrrr
talents = float(input("Enter the mass in talents: "))
pounds = float(input("Enter the mass in pounds: "))
lots = float(input("Enter the mass in lots: "))

# Conversion factors
pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot = 13.3

# Calculate the total mass in grams
total_grams = (talents * pounds_per_talent + pounds) * lots_per_pound * grams_per_lot

# Convert to kilograms and grams
kilograms = total_grams // 1000  # Integer division to get kilograms
grams = total_grams % 1000  # Get the remaining grams

# Print the result
print(f"The mass is approximately {kilograms} kilograms and {grams} grams.")