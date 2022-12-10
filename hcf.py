# This calculator finds the HCF of any given numbers.
# Made by Coder2011-ALT In Dec 2022
# Importing library
import time
# Defining variables
divisibilityList1 = []
divisibilityList2 = []
commonF = []

# Program heading
print("This is a HCF calculator.")

# Taking the input of the user
num1 = int(input("Write the first number-\n"))
num2 = int(input("Write the second number-\n"))

# Running the forloop to check the factors of the number.
for i in range(1, num1+1):
    if num1 % i == 0:
        divisibilityList1.append(i)
for j in range(1, num2+1):
    if num2 % j == 0:
        divisibilityList2.append(j)

# Running the forloop to check and append the common factors of the numbers
for k in divisibilityList1:
    for g in divisibilityList2:
        if g == k:
            commonF.append(g)
hcf = max(commonF)

# Checking and printing if the number are coprimes
if hcf != 1:
    print(f"The HCF of {num1} and {num2} is- \n{hcf}")
else:
    print(f"{num1} and {num2} are coprimes.")

# Time break between Thank you message
time.sleep(0.5)
print("Thank you!")
