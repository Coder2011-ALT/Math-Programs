# This calculator finds the factors of the number.
# Made by Coder2011-ALT In 2022

# Defining variables
divisibilityList = []
num = int(input("Write the number of which you want to check divisibility of-\n"))
factors = 0

# Running the forloop to check the factors of the number.
for i in range(1, num+1):
    if num % i == 0:
        print(f"{i} is a factor of {num}")
        divisibilityList.append(i)
        factors += 1

# Checking if the number is prime or composite
if factors > 2:
    print(f"{num} is a composite number.")
elif factors == 2:
    print(f"{num} is a prime number.")
elif factors < 2:
    print(f"{num} is prime nor composite number")

# Printing the factors of the number.
for j in divisibilityList:
    print(f"{j}",end=",")
print(f" are the factors of {num}")
print("Thank you!")
