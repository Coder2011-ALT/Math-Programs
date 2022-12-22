# This calculator findds the proportion  of two ratios
# Made by Coder2011-ALT in Dec 2022

# Importing library
import time

# Defining variables
num1 = 0
num2 = 0
num3 = 0
num4 = 0

# Program heading
print("This is a proportion calculator")

# Taking input from the user

print((f"Write in the format-\n num1:num2 num3:num4"))

num1 = int(input("Write the num1-\n"))
num2 = int(input("Write the num2-\n"))

num3 = int(input("Write the num3-\n"))
num4 = int(input("Write the num4-\n"))

if num1 * num4 == num3 * num2:
    print(f"{num1}:{num2}={num3}:{num4}")
else:
    print(f"{num1}:{num2}≠{num3}:{num4}")

time.sleep(0.5)
print("Thank you!")