def print_menu():
    print("====menu====")
    print("1. task 1")
    print("2. task 2")
    print("3. task 3")
    print("4. info")
    print("0. exit")


def menu():
    option = -1
    while (option != 0):
        print_menu()
        option = int(input("Введите номер: "))

        if (option == 0):
            break
        elif (option == 1):
            pass
        elif (option == 2):
            pass
        elif (option == 3):
            pass
        elif (option == 4):
            pass
