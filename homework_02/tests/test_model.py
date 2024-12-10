import pytest
from homework_02.mvc.model import Model
from homework_02.book import PhoneBook
from homework_02.resources.strings import FIELDS_MAP
from homework_02.tests.conftest import *


def test_open_book(setup_model_mocked_data_handler, setup_phonebook_true, setup_phonebook_false1,
                   setup_phonebook_false2):
    model = setup_model_mocked_data_handler
    book = model.open_book()
    assert book == setup_phonebook_true
    assert book != setup_phonebook_false1
    assert book != setup_phonebook_false2


def test_get_book(setup_model_mocked_data_handler, setup_phonebook_true, setup_phonebook_false1):
    model = setup_model_mocked_data_handler
    model._Model__phonebook = setup_phonebook_true
    book = model.get_book()
    assert book == setup_phonebook_true
    assert book != setup_phonebook_false1


def test_book_is_opened(setup_model_mocked_data_handler, setup_phonebook_true, setup_phonebook_empty):
    model = setup_model_mocked_data_handler
    assert not model.book_is_opened()

    model._Model__phonebook = setup_phonebook_true
    assert model.book_is_opened()

    model._Model__phonebook = setup_phonebook_empty
    assert model.book_is_opened() == False


def test_save_book(setup_model_mocked_data_handler, setup_phonebook_true):
    model = setup_model_mocked_data_handler
    model._Model__phonebook = setup_phonebook_true
    assert model.save_book()


def test_add_new_contact(setup_model_mocked_data_handler, setup_contact_input_data):
    model = setup_model_mocked_data_handler
    new_id = model.add_new_contact(setup_contact_input_data)

    # Assert that a valid ID was returned and the contact was added
    assert new_id == 1
    assert model.get_book().get_contact_by_id("1") is not None

    # Verify the contact's details
    contact = model.get_book().get_contact_by_id("1")
    assert contact.name == "John Doe"
    assert contact.phone == "81234567890"
    assert contact.comment == "Friend"
