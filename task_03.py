lst = []
while True:
    try:
        num = int(input("Enter a number: "))
        lst.append(num)
    except ValueError:
        break
        print("finish append numbers")
while True:
    print("""Menu:
    1. Display the list
    2. Get the maximum value in the list
    3. Get the minimum value in the list
    4. Display the value of an element by index
    5. Remove an element by index
    6. Exit""")

    choice = input("Choose an option: ")

    match choice:
        case '1':
            print("List:", lst)
        case '2':
            if len(lst) == 0:
                print("The list is empty")
            else:
                print("Maximum value in the list:", max(lst))
        case '3':
            if len(lst) == 0:
                print("The list is empty")
            else:
                print("Minimum value in the list:", min(lst))
        case '4':
            try:
                index = int(input("Enter the index of the element: "))
                print("Element at the entered index:", lst[index])
            except IndexError:
                print("Error: invalid index")
        case '5':
            try:
                index = int(input("Enter the index of the element to remove: "))
                del lst[index]
                print("Element removed successfully")
            except IndexError:
                print("Error: invalid index")
        case '6':
            print("Exiting the program")
            break
        case _:
            print("Invalid choice")
