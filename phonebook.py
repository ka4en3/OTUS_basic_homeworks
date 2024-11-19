import os.path

import json

JSON_FILENAME = "json/users_short.json"

MENU = ("Open phonebook",
        "Save phonebook",
        "Show contacts",
        "New contact",
        "Find contact",
        "Edit contact",
        "Delete contact",
        "Close and exit")

# global variable keeping Phonebook instance
book = {}
# global variable keeping field structure of Phonebook
fields = []
# divider for printing
divider = "-" * 50


def main():
    print_menu()
    choose_menu()


def print_menu():
    print(divider)
    for i in range(len(MENU)):
        print(f"{i + 1}. {MENU[i]}")


def choose_menu():
    user_input = input("-->: ")

    if user_input.isdigit() and 0 < int(user_input) < 9:
        user_input = int(user_input)

        # open phonebook
        if user_input == 1:
            if not book:
                open_book()
            else:
                if input("Phonebook is already opened! Do you want to overwrite? y/n ").strip().lower() == "y":
                    open_book()
                else:
                    print("Aborted.")
            print_menu()
            choose_menu()

        # save phonebook
        elif user_input == 2:
            if book:
                save_book()
            else:
                print("Phonebook is not opened!")
            print_menu()
            choose_menu()

        # show contacts
        elif user_input == 3:
            if book and len(book) > 0:
                print_book()
            else:
                print("Phonebook is empty or not opened!")
            print_menu()
            choose_menu()

        # new contact
        elif user_input == 4:
            if book:
                new_id = new_contact()
                if new_id:
                    print(f"Contact with ID {new_id} was successfully added.")
                else:
                    print(f"Something went wrong. Try again.")
            else:
                print("Phonebook is not opened!")
            print_menu()
            choose_menu()

        # find contact
        elif user_input == 5:
            if book and len(book) > 0:
                inp = input("Please enter Name, Phone or Company to find: ")
                find_contact(inp.strip().lower())
            else:
                print("Phonebook is empty or not opened!")
            print_menu()
            choose_menu()

        # edit contact
        elif user_input == 6:
            if book and len(book) > 0:
                inp = input("Please enter ID of contact to edit: ")
                if edit_contact(inp.strip()):
                    print(f"Contact with ID {inp} was successfully edited.")
                else:
                    print(f"Something went wrong. Try again.")
            else:
                print("Phonebook is empty or not opened!")
            print_menu()
            choose_menu()

        # delete contact
        elif user_input == 7:
            if book and len(book) > 0:
                inp = input("Please enter ID of contact to delete: ")
                if delete_contact(inp.strip()):
                    print(f"Contact with ID {inp} was deleted.")
            else:
                print("Phonebook is empty or not opened!")
            print_menu()
            choose_menu()

        # close and exit
        elif user_input == 8:
            exit()
    else:
        print("Incorrect input!")
        print_menu()
        choose_menu()


def open_book():
    global book

    if os.path.exists(JSON_FILENAME):
        print("Opening phone book...")

        with open(JSON_FILENAME, encoding="UTF-8") as file:
            book = json.load(file)

        if book and len(book) > 0:
            print("Book successfully opened!")
            get_fields()
            print_book()
        else:
            print("JSON is empty! Phonebook can't be open.")
    else:
        print("JSON file doesn't exist! Phonebook can't be open.")


def get_fields():
    fields.clear()
    contact0 = next(iter(book.values()))
    for key in dict(contact0).keys():
        fields.append(key)


def print_book():
    # print(divider)
    for cont_id, contact in book.items():
        print(divider)
        print(f"ID: {cont_id}")
        for key, value in contact.items():
            print(f"{key}: {value}")



def save_book():
    global book

    print("Saving phone book...")

    with open(JSON_FILENAME, "w", encoding="UTF-8") as file:
        json.dump(book, file, ensure_ascii=False, indent=4)

    print(f"Book successfully saved to file {JSON_FILENAME}!")


def new_contact():
    # Define the pattern for 8(999)999-99-99
    # pattern = r"^\d\(\d{3}\)\d{3}-\d{2}-\d{2}$"

    # to generate next contact_id
    next_id = str(max(int(k) for k in book.keys()) + 1)

    book[next_id] = {}
    for f in fields:
        inp = input(f"{f}: ")
        if f.strip().lower() in ("phone", "телефон"):
            temp = check_phone("".join(filter(str.isdigit, inp)))  # remove non digits
            if temp != '0':
                book[next_id][
                    f] = f"{temp[0]}({temp[1:4]}){temp[4:7]}-{temp[7:9]}-{temp[-2:]}"  # format phone number to 8(999)999-99-99
            else:  # to stop phone-input iteration
                book[next_id][f] = ""
        else:
            book[next_id][f] = inp

    return next_id


def check_phone(inp):
    if (inp.isdigit() and len(inp) == 11) or (inp.strip() == '0'):
        return inp
    else:
        inp = "".join(
            filter(str.isdigit, input("Please enter a correct phone number ('0' for skip): ")))  # remove non digits
        return check_phone(inp)


def edit_contact(edit_id):
    contact = book.get(edit_id)
    if contact:
        edit_id = edit_id
        for f in fields:
            inp = input(f"{f}: ")
            if f.strip().lower() in ("phone", "телефон"):
                temp = check_phone("".join(filter(str.isdigit, inp)))  # remove non digits
                if temp != '0':
                    book[edit_id][
                        f] = f"{temp[0]}({temp[1:4]}){temp[4:7]}-{temp[7:9]}-{temp[-2:]}"  # format phone number to 8(999)999-99-99
                else:  # to stop phone-input iteration
                    book[edit_id][f] = ""
            else:
                book[edit_id][f] = inp

        return edit_id
    else:
        print("Contact was not found!")
        return False


def find_contact(inp):
    print("Found contacts:")
    for cont_id, contact in book.items():
        found = 0
        for key, value in contact.items():
            if str(key).strip().lower() not in ("comment", "комментарий"):  # ignoring "Comment" field
                for word in str(value).strip().lower().split(sep=" "):
                    if inp in word:
                        print_contact(cont_id)
                        found = 1
                        break
            if found: break


def delete_contact(delete_id):
    contact = book.get(delete_id)
    if contact:
        book.pop(delete_id)
        return True
    else:
        print("Contact was not found!")
        return False


def print_contact(print_id):
    contact = book.get(print_id)
    if contact:
        print(divider)
        print(f"ID: {print_id}")
        for key, value in contact.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
