from homework_02.resources.strings import *


class View:
    @staticmethod
    def println(output: str):
        print(output)

    @staticmethod
    def user_input(input_message: str) -> str:
        return input(input_message)

    @staticmethod
    def print_menu():
        print(DIVIDER)
        print("\n".join(f"{i + 1}. {item}" for i, item in enumerate(MENU)))

    @staticmethod
    def print_book(book: dict):
        for cont_id, contact in book.items():
            print(f"{DIVIDER}\nID: {cont_id}")
            print("\n".join(f"{key}: {value}" for key, value in contact.items()))

    def input_new_contact(self):
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

