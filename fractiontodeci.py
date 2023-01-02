# This python application can convert fractions into decimals
# Made by Coder2011-ALT in Jan 2023

# Importing library
import time

# Defining variables
ans = 0

# Taking input from the user
numerator = int(input("Write the numerator of the fraction-\n"))
denominator = int(input("Write the denominator of the fraction-\n"))

# Doing calculations
ans = denominator / numerator
ans = round(ans, 3)

# Printing the answer
print(f"The decimal form of {numerator}/{denominator} is {ans}")
time.sleep(0.5)
print("Thank you!")
