from unittest.mock import patch, MagicMock
from homework_02.resources.strings import STR_OPENING, STR_INCORRECT_INPUT, STR_CONTACT_ADDED, STR_SAVED, STR_WRONG, \
    STR_FOUND_CONTACTS, DIVIDER, STR_CONTACT_NOT_FOUND, STR_CONTACT_EDITED, STR_CONTACT_DELETED


def test_start_invalid_input(setup_mocked_controller):
    controller = setup_mocked_controller
    controller.view.user_input.side_effect = ["invalid", "8"]
    controller.start()

    controller.view.println.assert_any_call(STR_INCORRECT_INPUT)


def test_start_1_8(setup_mocked_controller):
    # Mock user input to simulate valid menu actions and exit
    # with patch("homework_02.mvc.view.View.user_input", side_effect=["1", "8"]):  # Open book, then exit
    #     with patch("homework_02.mvc.view.View.print_menu") as mock_print_menu, \
    #             patch("homework_02.mvc.view.View.println") as mock_println, \
    #             patch("homework_02.mvc.model.Model.open_book", return_value=True):  # Simulate successful book opening

    controller = setup_mocked_controller
    controller.view.user_input.side_effect = ["1", "8"]
    controller.model.book_is_opened.return_value = False
    controller.start()

    assert controller.view.print_menu.call_count == 2
    assert controller.model.open_book.call_count == 1
    assert controller.view.print_book.call_count == 1
    assert controller.view.println.call_count == 1
    controller.view.println.assert_called_with(STR_OPENING)  # Check if opening message is printed


def test_start_1_y_8(setup_mocked_controller):
    controller = setup_mocked_controller
    controller.view.user_input.side_effect = ["1", "y", "8"]
    controller.model.book_is_opened.return_value = True
    controller.start()

    # Verify flow reached key points
    assert controller.view.print_menu.call_count == 2
    assert controller.model.open_book.call_count == 1
    assert controller.view.print_book.call_count == 1
    assert controller.view.println.call_count == 1
    controller.view.println.assert_called_with(STR_OPENING)  # Check if opening message is printed


def test_start_2_8(setup_mocked_controller):
    controller = setup_mocked_controller
    controller.view.user_input.side_effect = ["2", "8"]
    controller.model.book_is_opened.return_value = True
    controller.start()

    assert controller.model.save_book.call_count == 1
    assert controller.view.println.call_count == 2
    controller.view.println.assert_called_with(STR_SAVED)

    controller.view.user_input.side_effect = ["2", "8"]
    controller.model.save_book.return_value = False
    controller.start()
    assert controller.model.save_book.call_count == 2
    assert controller.view.println.call_count == 4
    controller.view.println.assert_called_with(STR_WRONG)


def test_start_3_8(setup_mocked_controller, setup_book_true_as_json):
    controller = setup_mocked_controller
    controller.view.user_input.side_effect = ["3", "8"]
    controller.model.book_is_opened.return_value = True
    controller.model.get_book.return_value = MagicMock(get_book_as_dict=lambda: setup_book_true_as_json)
    controller.start()
    assert controller.view.print_book.call_count == 1
    controller.view.print_book.assert_called_with(setup_book_true_as_json)


def test_start_4_8(setup_mocked_controller):
    controller = setup_mocked_controller
    controller.view.user_input.side_effect = ["4", "8"]
    controller.model.book_is_opened.return_value = True
    controller.view.input_contact.return_value = \
        {
            "name": "Name1",
            "phone": "79851475671",
            "comment": "Comment1"
        }
    controller.model.add_new_contact.return_value = 1
    controller.start()

    # Verify flow reached key points
    controller.model.add_new_contact.assert_called_with(
        {
            "name": "Name1",
            "phone": "79851475671",
            "comment": "Comment1"
        })
    assert controller.view.input_contact.call_count == 1
    assert controller.model.add_new_contact.call_count == 1
    controller.view.println.assert_called_with(STR_CONTACT_ADDED.format(new_id=1))


def test_start_5_8(setup_mocked_controller, setup_contact1, setup_contact2, setup_contact3):
    controller = setup_mocked_controller
    controller.view.user_input.side_effect = ["5", "str_to_find", "8"]
    controller.model.book_is_opened.return_value = True
    controller.model.find_contact_by_str.return_value = list[setup_contact1, setup_contact2, setup_contact3]
    controller.start()

    assert controller.view.user_input.call_count == 3
    assert controller.model.find_contact_by_str.call_count == 1
    controller.model.find_contact_by_str.assert_called_with("str_to_find")
    controller.view.println.assert_called_with(f"{STR_FOUND_CONTACTS}\n{DIVIDER}",
                                               list[setup_contact1, setup_contact2, setup_contact3], f"\n{DIVIDER}\n")


def test_start_6_8(setup_mocked_controller):
    controller = setup_mocked_controller
    controller.view.user_input.side_effect = ["6", "1", "8"]
    controller.model.book_is_opened.return_value = True
    controller.model.find_contact_by_id.return_value = False
    controller.start()
    controller.view.println.assert_called_with(STR_CONTACT_NOT_FOUND)

    controller.view.user_input.side_effect = ["6", "1", "8"]
    controller.model.find_contact_by_id.return_value = True
    controller.view.input_contact.return_value = \
        {
            "name": "Name2",
            "phone": "79851475671",
            "comment": "Comment2"
        }
    controller.model.edit_contact.return_value = True
    controller.start()
    # Verify flow reached key points
    controller.model.edit_contact.assert_called_with("1",
                                                     {
                                                         "name": "Name2",
                                                         "phone": "79851475671",
                                                         "comment": "Comment2"
                                                     })
    assert controller.view.input_contact.call_count == 1
    assert controller.model.edit_contact.call_count == 1
    controller.view.println.assert_called_with(STR_CONTACT_EDITED.format(edit_id=1))


def test_start_7_8(setup_mocked_controller):
    controller = setup_mocked_controller
    controller.view.user_input.side_effect = ["7", "1", "8"]
    controller.model.book_is_opened.return_value = True
    controller.model.find_contact_by_id.return_value = False
    controller.start()
    controller.view.println.assert_called_with(STR_CONTACT_NOT_FOUND)

    controller.view.user_input.side_effect = ["7", "1", "8"]
    controller.model.find_contact_by_id.return_value = True
    controller.model.delete_contact.return_value = True
    controller.start()
    # Verify flow reached key points
    controller.model.delete_contact.assert_called_with("1")
    assert controller.model.delete_contact.call_count == 1
    controller.view.println.assert_called_with(STR_CONTACT_DELETED.format(delete_id=1))


def test_book_is_opened(setup_mocked_controller):
    controller = setup_mocked_controller

    controller.model.book_is_opened.return_value = True
    assert controller.book_is_opened()

    controller.model.book_is_opened.return_value = False
    assert not controller.book_is_opened()
