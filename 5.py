
text = input("Enter a string: ").lower()

frequency = {}

for char in text:
    if char.isalpha():  
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

for letter, count in frequency.items():
    print(f"{letter} → {count}")
