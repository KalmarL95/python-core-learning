'''numbers = [1, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(numbers[0])
print(numbers[-1])

for n in numbers:
    print(n)

for n in numbers:
    if n > 5:
        print(n)

even_numbers = []

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers)'''


steps = [8000, 10000, 13000, 15000, 6000, 9000]

for n in steps:
   print(n)

for n in steps:
    if n >= 10000:
        print(n)

over_10k = []
for n in steps:
    if n >= 10000:
        over_10k.append(n)

print(over_10k)

email = " LEvEntE@gmail.com   "

clean_email = email.strip().lower()

print(clean_email)

