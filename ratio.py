# This calculator finds the ratio and proportion of any given two numbers.
# Made by Coder2011-ALT In Dec 2022
# Importing library
import time

# Program heading
print("This is a ratio calculator.")

# Taking the input of the user
num1 = int(input("Write the first number-\n"))
num2 = int(input("Write the second number-\n"))

# Definining variables
ans1 = num1
ans2 = num2

# Definining the ratio function
def ratio():
    # Defining variables and making them global
    global ans1
    global ans2
    divisibilityList1 = []
    divisibilityList2 = []
    commonF = []

    # Finding the HCF
    for i in range(1, ans1+1):
        if ans1 % i == 0:
            divisibilityList1.append(i)
    for j in range(1, ans2+1):
        if ans2 % j == 0:
            divisibilityList2.append(j)

    for k in divisibilityList1:
        for g in divisibilityList2:
            if g == k:
                commonF.append(g)
    hcf = max(commonF)

    # Dividing the both numbers with their HCF and if they are coprimes, print the result
    if hcf != 1:
        ans1 = int(ans1 / hcf)
        ans2 = int(ans2 / hcf)
        ratio()
    elif hcf == 1:
        print(f"The ratio of {num1} to {num2} is {ans1}:{ans2}")

# Calling the function
ratio()

# Time break between Thank you message
time.sleep(0.5)
print("Thank you!")