from unittest.mock import patch
import pytest
from homework_02.resources.strings import DIVIDER, FIELDS_MAP
from homework_02.mvc.view import View


def test_println(capsys):
    View.println("Testing string", ["object1", "object2", "object3"], "---")
    out, err = capsys.readouterr()
    assert out.strip() == "Testing string\nobject1---object2---object3"
    assert not err


def test_user_input():
    with patch("builtins.input", return_value="Test Input"):
        assert View.user_input("Enter something: ") == "test input"


def test_print_menu(capsys):
    View.print_menu()
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


def test_print_book(get_book_for_tests, capsys):
    View.print_book(get_book_for_tests)
    captured = capsys.readouterr()

    # sample_str = ""
    # for cid, contact in get_book_for_tests.items():
    #     sample_str = "".join([sample_str, f"{DIVIDER}\n{FIELDS_MAP['FIELD_ID']}: {cid}\n"])
    #     sample_str = "".join([sample_str, "\n".join(f"{key}: {value}" for key, value in contact.items())])
    #     sample_str = "".join([sample_str, "\n"])
    sample_str = "\n".join(
        [
            f"{DIVIDER}\n{FIELDS_MAP['FIELD_ID']}: {cid}\n" +
            "\n".join(f"{key}: {value}" for key, value in contact.items())
            for cid, contact in get_book_for_tests.items()
        ]
    ) + "\n"

    assert captured.out == sample_str


@pytest.mark.parametrize(
    "par1, par2",
    [
        (
                (s for s in ["test_name1", "89851475236", "test_comment1"]),
                {"name": "test_name1", "phone": "8(985)147-52-36", "comment": "test_comment1"}
        ),
        (
                (s for s in ["test_name2", "0", "test_comment2"]),
                {"name": "test_name2", "phone": "", "comment": "test_comment2"}
        )
    ]
)
def test_input_contact(par1, par2):
    with patch("builtins.input", lambda x: next(par1)):
        assert View.input_contact() == par2


def test_check_phone():
    assert View.check_phone("89127896978") == "89127896978"
    with patch("builtins.input", return_value="0"):
        assert View.check_phone("not_a_number") == '0'
