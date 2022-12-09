# This calculator finds the LCM of any two numbers
# Made by Coder2011-ALT in DEC 2022
# Importing library
import time
# Defining variables 
multiples1 = []
multiples2 = []
cm = []
lcm = 0

# Program heading
print("This is a LCM calculator.")

# Taking user input.
num1 = int(input("Write the first number-\n"))
num2 = int(input("Write the second number-\n"))

# Running the forloop to append the multiples of both numbers
for i in range(num1, num1*num2+1):
    if i % num1 == 0:
        multiples1.append(i)

for j in range(num2, num1*num2+1):
    if j % num2 == 0:
        multiples2.append(j)

# Running the forloop to append the common multiples of both numbers
for k in multiples1:
    for g in multiples2:
        if k == g:
            cm.append(g)
lcm = min(cm)

print(f"The LCM of {num1} and {num2} is -\n{lcm}")
time.sleep(0.5)
print("Thank you!")
