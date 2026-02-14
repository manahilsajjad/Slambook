import sys

def initial_slambook():
    rows, cols = int(input("Enter initial number of entries: ")), 5
    slambook = []
    for i in range(rows):
        print("\nEnter entry", i + 1)
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(input("Name*: "))
                if temp[j] == "" or temp[j] == " ":
                    sys.exit("Name is mandatory. Exiting...")
            if j == 1:
                temp.append(input("Nickname: ") or None)
            if j == 2:
                temp.append(input("Favorite thing: ") or None)
            if j == 3:
                temp.append(input("Least favorite thing: ") or None)
            if j == 4:
                temp.append(input("Favorite memory: ") or None)
        slambook.append(temp)
    return slambook

def menu():
    print("\n******** SLAMBOOK MENU ********")
    print("1. Add new entry")
    print("2. Remove an entry")
    print("3. Delete all entries")
    print("4. Search an entry")
    print("5. Display all entries")
    print("6. Exit")
    return int(input("Enter your choice: "))

def add_entry(sb):
    temp = []
    temp.append(input("Name: "))
    temp.append(input("Nickname: ") or None)
    temp.append(input("Favorite thing: ") or None)
    temp.append(input("Least favorite thing: ") or None)
    temp.append(input("Favorite memory: ") or None)
    sb.append(temp)
    return sb

def remove_entry(sb):
    name = input("Enter name to remove: ")
    for i in range(len(sb)):
        if name == sb[i][0]:
            print(sb.pop(i))
            print("Entry removed")
            return sb
    print("Entry not found")
    return sb

def delete_all(sb):
    sb.clear()
    return sb

def search_entry(sb):
    print("Search by:")
    print("1. Name")
    print("2. Nickname")
    choice = int(input("Enter choice: "))
    query = input("Enter search value: ")
    result = []
    index = 0 if choice == 1 else 1
    for entry in sb:
        if entry[index] == query:
            result.append(entry)
    if not result:
        return -1
    display_all(result)
    return 1

def display_all(sb):
    if not sb:
        print("Slambook is empty")
    else:
        for entry in sb:
            print(entry)

def exit_program():
    print("Thank you for using the Slambook!")
    sys.exit()

print("Welcome to the Slambook Project")
sb = initial_slambook()
choice = 1

while choice in (1, 2, 3, 4, 5):
    choice = menu()
    if choice == 1:
        sb = add_entry(sb)
    elif choice == 2:
        sb = remove_entry(sb)
    elif choice == 3:
        sb = delete_all(sb)
    elif choice == 4:
        if search_entry(sb) == -1:
            print("No matching entry found")
    elif choice == 5:
        display_all(sb)
    else:
        exit_program()
