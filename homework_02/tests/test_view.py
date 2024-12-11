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


def test_print_book(setup_book_true_as_json, capsys):
    View.print_book(setup_book_true_as_json)
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
            for cid, contact in setup_book_true_as_json.items()
        ]
    ) + "\n"

    assert captured.out == sample_str


@pytest.mark.parametrize(
    "inp, result",
    [
        (
            (s for s in ["test_name1", "89851475236", "test_comment1"]),
            {FIELDS_MAP["FIELD_NAME"]: "test_name1", FIELDS_MAP["FIELD_PHONE"]: "8(985)147-52-36", FIELDS_MAP["FIELD_COMMENT"]: "test_comment1"}
        ),
        (
            (s for s in ["test_name2", "0", "test_comment2"]),
            {FIELDS_MAP["FIELD_NAME"]: "test_name2", FIELDS_MAP["FIELD_PHONE"]: "", FIELDS_MAP["FIELD_COMMENT"]: "test_comment2"}
        )
    ]
)
def test_input_contact(inp, result):
    with patch("builtins.input", lambda x: next(inp)):
        assert View.input_contact() == result


def test_check_phone():
    assert View.check_phone("89127896978") == "89127896978"
    with patch("builtins.input", return_value="0"):
        assert View.check_phone("not_a_number") == '0'
