# A: Write a program to check whether an alphabet is a vowel or constant

letter = input("Input a letter of the alphabet: ")
if letter.lower() in ('a','e','i','o','u'):
    print(f"The letter '{letter}' is a vowel.")

elif letter.lower() == 'y':
    print("Sometimes the letter y stands for a vowel, sometimes stands for a constant.")

else:
    print(f"The letter '{letter}' is a constant.")

# B: Write a Python program to find those numbers which are divisible by 7 and a multiple of 5, between 5 and 2700.

n = []

for i in range(5, 2700):
    if(i % 7 == 0) and (i % 5 == 0):
        n.append(str(i)) 

print(','.join(n))