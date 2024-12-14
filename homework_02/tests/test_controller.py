from unittest.mock import patch, MagicMock
from homework_02.resources.strings import STR_OPENING, STR_INCORRECT_INPUT, STR_CONTACT_ADDED, STR_SAVED, STR_WRONG


def test_book_is_opened(setup_mocked_controller):
    controller = setup_mocked_controller

    controller.model.book_is_opened.return_value = True
    assert controller.book_is_opened()

    controller.model.book_is_opened.return_value = False
    assert not controller.book_is_opened()


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
    controller.model.get_book.get_book_as_dict.return_value = MagicMock(get_book_as_dict=lambda: {})
    controller.start()
    assert controller.view.print_book.call_count == 1
    # controller.view.print_book.assert_called_with(setup_book_true_as_json)
    controller.view.print_book.assert_called_with("{}")

    # patch("homework_02.mvc.model.Model.get_book", return_value=MagicMock(get_book_as_dict=lambda: {})),


def test_new_contact(setup_mocked_controller):
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


