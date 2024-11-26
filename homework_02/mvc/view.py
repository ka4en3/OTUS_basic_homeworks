from homework_02.resources.strings import *


class View:
    @staticmethod
    def println(output: str, objects: list = None, sep: str = ""):
        if output: print(output)
        if objects is not None: print(*objects, sep=sep)

    @staticmethod
    def user_input(input_message: str) -> str:
        return input(input_message)

    @staticmethod
    def print_menu():
        print(DIVIDER)
        print("\n".join(f"{i + 1}. {item}" for i, item in enumerate(MENU)))

    @staticmethod
    def print_book(book: dict):
        for cid, contact in book.items():
            print(f"{DIVIDER}\n{FIELDS_MAP['FIELD_ID']}: {cid}")
            print("\n".join(f"{key}: {value}" for key, value in contact.items()))

    @staticmethod
    def input_contact() -> dict:
        fields_dict = {}
        for f in [v for v in FIELDS_MAP.values() if v != FIELDS_MAP['FIELD_ID']]:  # all fields except ID
            inp = input(f"{f}: ")
            if f.strip().lower() in ("phone", "телефон"):
                temp = View.check_phone("".join(filter(str.isdigit, inp)))  # remove non digits
                if temp != '0':
                    fields_dict[
                        f] = f"{temp[0]}({temp[1:4]}){temp[4:7]}-{temp[7:9]}-{temp[-2:]}"  # format phone number to 8(999)999-99-99
                else:  # to stop phone-input iteration
                    fields_dict[f] = ""
            else:
                fields_dict[f] = inp
        return fields_dict

    @staticmethod
    def check_phone(inp: str) -> str:
        if (inp.isdigit() and len(inp) == 11) or (inp.strip() == '0'):
            return inp
        else:
            inp = "".join(
                filter(str.isdigit, input("Please enter a correct phone number ('0' for skip): ")))  # remove non digits
            return View.check_phone(inp)
