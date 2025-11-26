numbers = [12, 25, 40, 42, 55, 18, 30]

for n in numbers:
    if n > 50:
        break
    if n % 5 == 0:
        continue
    print(n)
