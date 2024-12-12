from unittest.mock import patch


def test_book_is_opened(setup_mocked_controller):
    controller = setup_mocked_controller

    controller.model.book_is_opened.return_value = True
    assert controller.book_is_opened()

    controller.model.book_is_opened.return_value = False
    assert not controller.book_is_opened()


def test_start(setup_mocked_controller, capsys):
    controller = setup_mocked_controller
    controller.start()
    out, err = capsys.readouterr()
    assert not err
    assert out == ("--------------------------------------------------\n"
                   "1. Open phonebook\n"
                   "2. Save phonebook\n"
                   "3. Show contacts\n"
                   "4. New contact\n"
                   "5. Find contact\n"
                   "6. Edit contact\n"
                   "7. Delete contact\n"
                   "8. Close and exit\n")

    with patch("builtins.input", ["1", "2", "3", "4", "5", "6", "7", "8"]) as inp:
        return_value = inp[7]
