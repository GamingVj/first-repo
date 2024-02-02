# It is used to find if the given number is prime or no

number=int(input("Enter a number.\n-->"))

if number<2:
    print(f"{number} is not prime number")

else:
    is_prime=True

for i in range(2, (int (number**0.5))+1):
    if number%i==0:
        is_prime=False
        break

if is_prime:
    print(f"{number} is prime")

else:
    print(f"{number} is not prime")