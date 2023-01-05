# This python application can convert decimals into fractions
# Made by Coder2011-ALT in Jan 2023

# Importing libraries
import time

# Asking the user's input
deci = input("Write a decimal which you want to convert in fraction-\n")

# Defining variables
decilen = 0
deciValue = 0
decilength = 0 
num_zero = 0
hcf = 0
denominator = 1
divisibilityList1 = []
divisibilityList2 = []
commonF = []

# Running the condition to check if it has decimal point or not and calculating what will be its denominator through a forloop
if "." in deci:
    deciValue = deci.find(".")
    decilen = len(deci)
    num_zero = (decilen - deciValue) - 1
    # Running the forloop to make the denominator
    for i in range(0, num_zero):
        denominator *= 10
    deci = deci.replace(".", "")
    # Typecasting the decimal to integer for further operations
    deci = int(deci)
    # Running the forloop to check the factors of the number.
    for i in range(1, deci+1):
        if deci % i == 0:
            divisibilityList1.append(i)
    for j in range(1, denominator+1):
        if denominator % j == 0:
            divisibilityList2.append(j)

    # Running the forloop to check and append the common factors of the numbers
    for k in divisibilityList1:
        for g in divisibilityList2:
            if g == k:
                commonF.append(g)
    hcf = max(commonF)
    deci /= hcf
    denominator /= hcf

# Converting the variables to integer so that it does not show the float values
deci = int(deci)
denominator = int(denominator)
# Printing the result
print(f"The numerator and denominator of {deci} is {deci} and {denominator} respectively.")

# Thank you message
time.sleep(0.5)
print("Thank you.")
