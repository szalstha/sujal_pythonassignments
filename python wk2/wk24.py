books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10
}

name = input("Enter book name: ")

if name not in books:
    print("Unavailable")
else:
    while True:
        copies = input("Enter number of copies: ")
        if copies.isdigit():
            copies = int(copies)
            break
        else:
            print("Please enter a valid number.")

    if books[name] >= copies:
        print("Available")
    elif books[name] > 0:
        print("Partially Available")
    else:
        print("Unavailable")
