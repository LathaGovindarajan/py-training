def write_file():
    filename = input("Enter the filename: ")
    data = input("Enter the content to write:\n")
    with open(filename, 'w') as f:
        f.write(data)
    print(f"Data written to {filename} successfully.")

def read_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(" File Content ")
            print(content)
    except FileNotFoundError:
        print("File not found")

def append_file():
    filename = input("Enter the filename: ")
    data = input("Enter the content to append:")
    with open(filename, 'a') as f:
        f.write(data)
    print(f"Data appended to {filename} successfully.")

while True:
    print("Menu:")
    print("1.Write to a file")
    print("2.Read from a file")
    print("3.Append to a file")
    print("4.Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        write_file()
    elif choice == '2':
        read_file()
    elif choice == '3':
        append_file()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
