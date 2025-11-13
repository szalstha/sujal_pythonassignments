password = input("Enter your password: ")

has_letter = any(ch.isalpha() for ch in password)
has_number = any(ch.isdigit() for ch in password)
has_special = any(ch in "@#$%&" for ch in password)


if len(password) < 6 or password.isalpha():
    print("Password Strength: Weak")
elif len(password) >= 6 and has_letter and has_number and not has_special:
    print("Password Strength: Moderate")
elif len(password) >= 8 and has_letter and has_number and has_special:
    print("Password Strength: Strong")
else:
    print("Password Strength: Weak")
