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
