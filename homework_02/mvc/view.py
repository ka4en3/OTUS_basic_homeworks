from homework_02.resources.strings import DIVIDER, FIELDS_MAP, MENU


class View:
    """
    The View class is responsible for handling all user interactions.
    It provides methods for displaying information, receiving user input, and formatting the display.
    """

    @staticmethod
    def println(output: str, objects: list = None, sep: str = ""):
        """
        Prints the given output and additional objects to the console.

        Args:
            output (str): The string to be printed.
            objects (list, optional): A list of objects to be printed after the output. Defaults to None.
            sep (str, optional): The separator to be used between objects. Defaults to an empty string.
        """
        if output:
            print(output)
        if objects is not None:
            print(*objects, sep=sep)

    @staticmethod
    def user_input(input_message: str) -> str:
        """
        Prompts the user for input and returns the response after converting it to lowercase and stripping whitespace.

        Args:
            input_message (str): The message to display to the user when requesting input.

        Returns:
            str: The user input, processed to lowercase and stripped of surrounding whitespace.
        """
        return input(input_message).lower().strip()

    @staticmethod
    def print_menu():
        """
        Displays the main menu to the user by printing a list of available options.
        """
        print(DIVIDER)
        print("\n".join(f"{i + 1}. {item}" for i, item in enumerate(MENU)))

    @staticmethod
    def print_book(book: dict):
        """
        Prints the details of each contact in the phone book.

        Args:
            book (dict): A dictionary of contacts where the key is the contact ID and the value is the contact's information.
        """
        for cid, contact in book.items():
            print(f"{DIVIDER}\n{FIELDS_MAP['FIELD_ID']}: {cid}")
            print("\n".join(f"{key}: {value}" for key, value in contact.items()))

    @staticmethod
    def input_contact() -> dict:
        """
        Prompts the user to input details for a new contact and returns the data as a dictionary.

        Returns:
            dict: A dictionary containing the contact's details (fields such as name, phone, etc.).
        """
        fields_dict = {}
        for f in [
            v for v in FIELDS_MAP.values() if v != FIELDS_MAP["FIELD_ID"]
        ]:  # all fields except ID
            inp = input(f"{f}: ")
            if f.strip().lower() in ("phone", "телефон"):
                temp = View.check_phone(
                    "".join(filter(str.isdigit, inp))
                )  # remove non-digits
                if temp != "0":
                    # format phone number to 8(999)999-99-99
                    fields_dict[f] = (
                        f"{temp[0]}({temp[1:4]}){temp[4:7]}-{temp[7:9]}-{temp[-2:]}"
                    )
                else:  # to stop phone-input iteration
                    fields_dict[f] = ""
            else:
                fields_dict[f] = inp
        return fields_dict

    @staticmethod
    def check_phone(inp: str) -> str:
        """
        Validates and formats a phone number input. Ensures the input is 11 digits or '0' for skipping.

        Args:
            inp (str): The phone number input, which is stripped of non-digit characters.

        Returns:
            str: A valid phone number if the input is correct, otherwise prompts the user to enter a valid number.
        """
        while not ((inp.isdigit() and len(inp) == 11) or (inp.strip() == "0")):
            inp = "".join(
                filter(
                    str.isdigit,
                    input("Please enter a correct phone number ('0' for skip): "),
                )
            )
        return inp
