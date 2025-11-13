
name = input("Enter your full name: ").strip()


parts = name.split()

if len(parts) >= 2:
    first_initial = parts[0][0].upper()
    last_initial = parts[-1][0].upper()
    print(f"Your initials are: {first_initial}.{last_initial}")
else:
    print("Please enter both your first and last name.")
