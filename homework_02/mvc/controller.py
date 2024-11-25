from homework_02.mvc.model import Model
from homework_02.mvc.view import View
from homework_02.mvc.json_handler import JSONHandler
from homework_02.resources.strings import *


class Controller:
    def __init__(self):
        #   controller keeps reference to both model and view
        self.model = Model(JSONHandler(JSON_FILENAME))  # JSONHandler in our case
        self.view = View  # View has all methods static

    def start(self):
        self.view.print_menu()
        self.choose_menu()

    def choose_menu(self):
        user_input = self.view.user_input("-->: ")

        if user_input.isdigit() and 0 < int(user_input) < 9:
            user_input = int(user_input)

            # open phonebook
            if user_input == 1:
                if not self.model.book_is_opened():
                    book = self.model.open_book()
                    if book:
                        self.view.print_book(book.get_book_as_dict())
                else:
                    if self.view.user_input(STR_PHONEBOOK_ALREADY_OPENED).strip().lower() == "y":
                        book = self.model.open_book()
                        if book:
                            self.view.print_book(book.get_book_as_dict())
                    else:
                        self.view.println(STR_ABORTED)

            # save phonebook
            elif user_input == 2:
                if self.model.book_is_opened():
                    self.model.save_book()
                else:
                    self.view.println(STR_PHONEBOOK_NOT_OPENED)

            # show contacts
            elif user_input == 3:
                if self.model.book_is_opened():
                    self.view.print_book(self.model.get_book().get_book_as_dict())
                else:
                    print(STR_PHONEBOOK_NOT_OPENED)

            # new contact
            elif user_input == 4:
                if self.model.book_is_opened():
                    new_id = self.model.add_new_contact(self.view.input_contact())
                    self.view.println(STR_CONTACT_ADDED.format(new_id=new_id) if new_id else STR_WRONG)
                else:
                    self.view.println(STR_PHONEBOOK_NOT_OPENED)

            # # find contact
            # elif user_input == 5:
            #     if book and len(book) > 0:
            #         inp = input("Please enter Name, Phone or Company to find: ")
            #         find_contact(inp.strip().lower())
            #     else:
            #         print("Phonebook is empty or not opened!")
            #     print_menu()
            #     choose_menu()
            #
            # # edit contact
            # elif user_input == 6:
            #     if book and len(book) > 0:
            #         inp = input("Please enter ID of contact to edit: ")
            #         if edit_contact(inp.strip()):
            #             print(f"Contact with ID {inp} was successfully edited.")
            #         else:
            #             print(f"Something went wrong. Try again.")
            #     else:
            #         print("Phonebook is empty or not opened!")
            #     print_menu()
            #     choose_menu()
            #
            # # delete contact
            # elif user_input == 7:
            #     if book and len(book) > 0:
            #         inp = input("Please enter ID of contact to delete: ")
            #         if delete_contact(inp.strip()):
            #             print(f"Contact with ID {inp} was deleted.")
            #     else:
            #         print("Phonebook is empty or not opened!")
            #     print_menu()
            #     choose_menu()

            # close and exit
            elif user_input == 8:
                exit()
        else:
            self.view.println(STR_INCORRECT_INPUT)

        # on complete of every step print menu again
        self.view.print_menu()
        self.choose_menu()
