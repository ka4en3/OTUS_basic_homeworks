from homework_02.mvc.view import View
from homework_02.mvc.model import Model
from homework_02.mvc.json_handler import JSONHandler
from homework_02.resources.strings import *


class Controller:
    """
    The Controller class coordinates between the model and view.
    It handles user inputs and manages the flow of the application.
    """

    def __init__(self):
        """
        Initializes the controller by creating references to the model and view.
        The model is responsible for data management and the view handles user interaction.
        """
        #   controller keeps reference to both model and view
        self.model = Model(JSONHandler(JSON_FILENAME))  # JSONHandler in our case
        self.view = View  # View has all methods static

    def start(self):
        """
        Starts the application by displaying the menu and prompting user interaction.
        """
        self.view.print_menu()
        self.choose_menu()

    def choose_menu(self):
        """
        Processes the user's menu choice and performs the corresponding action.

        This method handles user input, validates it, and calls the necessary
        methods from the model and view to manage contacts in the phone book.
        """
        user_choice = self.view.user_input("-->: ")

        if user_choice.isdigit() and 0 < int(user_choice) < 9:
            user_choice = int(user_choice)

            # open phonebook
            if user_choice == 1:
                self.view.println(STR_OPENING)
                if not self.model.book_is_opened():
                    book = self.model.open_book()
                    (
                        self.view.print_book(book.get_book_as_dict())
                        if book
                        else self.view.println(STR_WRONG)
                    )
                else:
                    if self.view.user_input(STR_ALREADY_OPENED) == "y":
                        book = self.model.open_book()
                        (
                            self.view.print_book(book.get_book_as_dict())
                            if book
                            else self.view.println(STR_WRONG)
                        )
                    else:
                        self.view.println(STR_ABORTED)

            # save phonebook
            elif user_choice == 2:
                self.view.println(STR_SAVING)
                if self.model.book_is_opened() and self.model.save_book():
                    self.view.println(STR_SAVED)
                else:
                    self.view.println(STR_SAVING_ERROR)

            # show contacts
            elif user_choice == 3:
                if self.model.book_is_opened():
                    self.view.print_book(self.model.get_book().get_book_as_dict())
                else:
                    self.view.println(STR_NOT_OPENED)

            # new contact
            elif user_choice == 4:
                if self.model.book_is_opened():
                    input_contact = self.view.input_contact()
                    new_id = self.model.add_new_contact(input_contact)
                    self.view.println(
                        STR_CONTACT_ADDED.format(new_id=new_id) if new_id else STR_WRONG
                    )
                else:
                    self.view.println(STR_NOT_OPENED)

            # find contact
            elif user_choice == 5:
                if self.model.book_is_opened():
                    str_to_find = self.view.user_input(STR_INPUT_TO_FIND)
                    found_contacts = self.model.find_contact_by_str(str_to_find)
                    self.view.println(
                        f"{STR_FOUND_CONTACTS}\n{DIVIDER}", found_contacts, f"\n{DIVIDER}\n"
                        if found_contacts is not None
                        else self.view.println(STR_WRONG)
                    )
                else:
                    self.view.println(STR_NOT_OPENED)

            # edit contact
            elif user_choice == 6:
                if not self.model.book_is_opened():
                    self.view.println(STR_NOT_OPENED)
                else:
                    edit_id = self.view.user_input(STR_INPUT_TO_EDIT)
                    if not self.model.find_contact_by_id(edit_id):
                        self.view.println(STR_CONTACT_NOT_FOUND)
                    else:
                        input_contact = self.view.input_contact()
                        success = self.model.edit_contact(edit_id, input_contact)
                        self.view.println(
                            STR_CONTACT_EDITED.format(edit_id=edit_id)
                            if success
                            else STR_WRONG
                        )

            # delete contact
            elif user_choice == 7:
                if not self.model.book_is_opened():
                    self.view.println(STR_NOT_OPENED)
                else:
                    delete_id = self.view.user_input(STR_INPUT_TO_DELETE)
                    if not self.model.find_contact_by_id(delete_id):
                        self.view.println(STR_CONTACT_NOT_FOUND)
                    else:
                        success = self.model.delete_contact(delete_id)
                        self.view.println(
                            STR_CONTACT_DELETED.format(delete_id=delete_id)
                            if success
                            else STR_WRONG
                        )

            # close and exit
            elif user_choice == 8:
                exit()
        else:
            self.view.println(STR_INCORRECT_INPUT)

        # on complete of every step print menu again
        self.view.print_menu()
        self.choose_menu()
