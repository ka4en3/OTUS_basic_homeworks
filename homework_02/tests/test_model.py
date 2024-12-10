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


def test_add_new_contact(setup_model_mocked_data_handler, setup_phonebook_true, setup_contact_input_data,
                         setup_contact3):
    model = setup_model_mocked_data_handler
    model._Model__phonebook = setup_phonebook_true
    new_id = model.add_new_contact(setup_contact_input_data)

    # Assert that a valid ID was returned and the contact was added
    assert new_id == int(setup_contact3.id) + 1
    contact = model.get_book().get_contact_by_id(str(new_id))
    assert contact

    # Verify the contact's details
    assert contact.name == setup_contact_input_data[FIELDS_MAP["FIELD_NAME"]]
    assert contact.phone == setup_contact_input_data[FIELDS_MAP["FIELD_PHONE"]]
    assert contact.comment == setup_contact_input_data[FIELDS_MAP["FIELD_COMMENT"]]


def test_edit_contact(setup_model_mocked_data_handler, setup_phonebook_true, setup_contact_input_data, setup_contact3):
    model = setup_model_mocked_data_handler
    model._Model__phonebook = setup_phonebook_true
    model.edit_contact(setup_contact3.id, setup_contact_input_data)

    contact = model.get_book().get_contact_by_id(setup_contact3.id)
    assert contact

    # Verify the contact's details
    assert contact.name == setup_contact_input_data[FIELDS_MAP["FIELD_NAME"]]
    assert contact.phone == setup_contact_input_data[FIELDS_MAP["FIELD_PHONE"]]
    assert contact.comment == setup_contact_input_data[FIELDS_MAP["FIELD_COMMENT"]]


def test_find_contact_by_id(setup_model_mocked_data_handler, setup_phonebook_true, setup_contact1):
    model = setup_model_mocked_data_handler
    model._Model__phonebook = setup_phonebook_true

    contact = model.find_contact_by_id("1001")
    assert not contact

    contact = model.find_contact_by_id(setup_contact1.id)
    assert contact
    assert contact.id == setup_contact1.id


def test_find_contact_by_str(setup_model_mocked_data_handler, setup_phonebook_true, setup_contact1, setup_contact2, setup_contact3):
    model = setup_model_mocked_data_handler
    model._Model__phonebook = setup_phonebook_true

    contact_list = model.find_contact_by_str("abracadabra")
    assert len(contact_list) == 0

    contact_list = model.find_contact_by_str(setup_contact1.comment[10:14])
    assert len(contact_list) == 1
    assert contact_list[0].id == setup_contact1.id

    contact_list = model.find_contact_by_str("1")
    assert len(contact_list) == 2
    assert contact_list[0].id == setup_contact1.id
    assert contact_list[1].id == setup_contact3.id

    contact_list = model.find_contact_by_str("кас")
    assert len(contact_list) == 3
    assert contact_list[0].id == setup_contact1.id
    assert contact_list[1].id == setup_contact2.id
    assert contact_list[2].id == setup_contact3.id


def test_delete_contact(setup_model_mocked_data_handler, setup_phonebook_true, setup_contact1, setup_contact2, setup_contact3):
    model = setup_model_mocked_data_handler
    model._Model__phonebook = setup_phonebook_true

    assert not model.delete_contact("111")

    assert model.delete_contact(setup_contact2.id)
    assert model.get_book().get_size() == 2
    assert model.get_book().get_contact_by_id(setup_contact1.id)
    assert not model.get_book().get_contact_by_id(setup_contact2.id)
    assert model.get_book().get_contact_by_id(setup_contact3.id)