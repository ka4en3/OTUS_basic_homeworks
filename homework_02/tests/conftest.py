# from helpers.utils import add_homework_path
#
# add_homework_path(__file__)

from unittest.mock import Mock
import pytest
from homework_02.mvc.model import Model
from homework_02.book import PhoneBook
from homework_02.book import Contact
from homework_02.resources.strings import FIELDS_MAP


@pytest.fixture(scope="session", autouse=True)
def setup_book_as_json() -> dict:
    return {
        "235": {
            "Name": "Андрианов Александр Даниилович",
            "Phone": "+7(993)785-20-82",
            "Company": "Мультиметры",
            "Comment": "Кас harass situ Aubrey 1"
        },
        "236": {
            "Name": "Касьянова Александра Александровна",
            "Phone": "+7(495)758-82-47",
            "Company": "Стремглав",
            "Comment": "notify caveat scuff"
        },
        "237": {
            "Name": "Лукина Елизавета Никитична",
            "Phone": "+7(940)465-14-13",
            "Company": "Кожухи",
            "Comment": "planetaria lympКасh Jonathan"
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
    return Contact("238", "wrong_name", " ", "wrong wrong wrong")


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
def setup_model_mocked_data_handler(setup_book_as_json):
    # Mock the data handler
    mock_data_handler = Mock()
    mock_data_handler.load_data_to_dict.return_value = setup_book_as_json
    mock_data_handler.save_data_to_file.return_value = True
    # Initialize model with mock data handler
    model = Model(mock_data_handler)
    return model
