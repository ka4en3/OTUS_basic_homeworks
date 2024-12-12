# from helpers.utils import add_homework_path
#
# add_homework_path(__file__)
from unittest.mock import Mock
import pytest
import json
from homework_02.mvc.model import Model
from homework_02.book.phone_book import PhoneBook
from homework_02.book.contact import Contact
from homework_02.resources.strings import FIELDS_MAP

TEMP_JSON_FILENAME = "users_test_save_to_file.json"


@pytest.fixture(scope="session", autouse=True)
def setup_book_true_as_json() -> dict:
    return {
        "235": {
            "name": "Андрианов Александр Даниилович",
            "phone": "+7(993)785-20-82",
            "comment": "Кас harass situ Aubrey 1"
        },
        "236": {
            "name": "Касьянова Александра Александровна",
            "phone": "+7(495)758-82-47",
            "comment": "notify caveat scuff"
        },
        "237": {
            "name": "Лукина Елизавета Никитична",
            "phone": "+7(940)465-14-13",
            "comment": "planetaria lympКасh Jonathan"
        }
    }


@pytest.fixture(scope="session", autouse=True)
def setup_book_false_as_json() -> dict:
    return {
        "235": {
            "name": "Андрианов Александр Даниилович",
            "phone": "+7(993)785-20-82",
            "comment": "Кас harass situ Aubrey 1"
        },
        "236": {
            "name": "Касьянова Александра Александровна",
            "phone": "+7(495)758-82-47",
            "comment": "notify caveat scuff"
        },
        "237": {
            "name": "Лукина Елизавета Никитична",
            "phone": "+7(940)465-14-13",
            "comment": "planetaria lympКасh Jonathan"
        },
        "238": {
            "name": "wrong_name",
            "phone": "1",
            "comment": "wrong wrong wrong"
        }
    }


@pytest.fixture(scope="session", autouse=True)
def setup_contact_input_data() -> dict:
    # Define a new contact's input data
    return {
        FIELDS_MAP["FIELD_NAME"]: "Миронова Маргарита Вячеславовна",
        FIELDS_MAP["FIELD_PHONE"]: "+7(919)213-82-25",
        FIELDS_MAP["FIELD_COMMENT"]: "damnation dogmatism enjoinder",
    }


@pytest.fixture(scope="function", autouse=True)
def setup_contact1():
    return Contact("235", "Андрианов Александр Даниилович", "+7(993)785-20-82", "Кас harass situ Aubrey 1")


@pytest.fixture(scope="function", autouse=True)
def setup_contact2():
    return Contact("236", "Касьянова Александра Александровна", "+7(495)758-82-47", "notify caveat scuff")


@pytest.fixture(scope="function", autouse=True)
def setup_contact3():
    return Contact("237", "Лукина Елизавета Никитична", "+7(940)465-14-13", "planetaria lympКасh Jonathan")


@pytest.fixture(scope="function", autouse=True)
def setup_contact4():
    return Contact("238", "wrong_name", "1", "wrong wrong wrong")


@pytest.fixture(scope="function", autouse=True)
def setup_phonebook_true(setup_contact1, setup_contact2, setup_contact3):
    book = PhoneBook()
    book.add_to_book(setup_contact1)
    book.add_to_book(setup_contact2)
    book.add_to_book(setup_contact3)
    return book


@pytest.fixture(scope="function", autouse=True)
def setup_phonebook_false1(setup_contact1, setup_contact2, setup_contact3, setup_contact4):
    book = PhoneBook()
    book.add_to_book(setup_contact1)
    book.add_to_book(setup_contact2)
    book.add_to_book(setup_contact3)
    book.add_to_book(setup_contact4)
    return book


@pytest.fixture(scope="function", autouse=True)
def setup_phonebook_false2(setup_contact1, setup_contact2):
    book = PhoneBook()
    book.add_to_book(setup_contact1)
    book.add_to_book(setup_contact2)
    book.add_to_book(setup_contact1)
    return book


@pytest.fixture(scope="function", autouse=True)
def setup_phonebook_empty():
    return PhoneBook()


@pytest.fixture(scope="function", autouse=True)
def setup_model_mocked_data_handler(setup_book_true_as_json):
    # Mock the data handler
    mock_data_handler = Mock()
    mock_data_handler.load_data_to_dict.return_value = setup_book_true_as_json
    mock_data_handler.save_data_to_file.return_value = True
    # Initialize model with mock data handler
    model = Model(mock_data_handler)
    return model


@pytest.fixture(scope="function")
def setup_empty_json_file_for_tests(tmp_path):
    with open(filepath := tmp_path / TEMP_JSON_FILENAME, "x", encoding="UTF-8") as file:
        file.write("{}")
    return filepath


@pytest.fixture(scope="function")
def setup_json_file_with_data_for_tests(tmp_path, setup_book_true_as_json):
    with open(filepath := tmp_path / TEMP_JSON_FILENAME, "x", encoding="UTF-8") as file:
        json.dump(setup_book_true_as_json, file, ensure_ascii=False, indent=4)
    return filepath


@pytest.fixture(scope="function")
def setup_json_file_with_wrong_data_for_tests(tmp_path, setup_book_true_as_json):
    with open(filepath := tmp_path / "malformed.json", "x", encoding="UTF-8") as file:
        file.write("{malformed_json: true}")  # Invalid JSON syntax
    return filepath
