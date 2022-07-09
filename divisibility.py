# This calculator checks that from which number the number is divisible by and checks the number whether it is prime or composite.
# Made by Coder2011-ALT In 2022
# Defining variables
divisibilityList = []
num = int(input("Write the number of which you want to check divisibility of-\n"))
prime = 0
# Running the forloop to check the factors of the number.
for i in range(1, num+1):
    if num % i == 0:
        print(f"{i} is divisible by {num}")
        divisibilityList.append(i)
        prime += 1
# Checking if the number is prime or composite
if prime > 2:
    print(f"{num} is a composite number.")
elif prime == 2:
    print(f"{num} is a prime number.")
elif prime < 2:
    print(f"{num} is prime nor composite number")
# Printing the factors of the number.
print(f"The numbers - \n{divisibilityList} are divisible by {num}")
