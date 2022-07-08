import time
num = int(input("Write the number of which you want to check divisibility of-\n"))
divisibilityNum = int(input("Write the number that you want the number is divisible to numbers till-\n"))
prime = 0
for i in range(1, divisibilityNum):
    if num % i == 0:
        print(f"{i} is divisible by {num}")
if divisibilityNum < num:
    print(f"{num} is divisible by {num}")
for j in range(2, num):
    prime += 1
if prime > 2:
    print(f"{num} is a composite number.")
elif prime == 2:
    print(f"{num} is a prime number.")
elif prime < 2:
    print(f"{num} is prime nor composite number")
