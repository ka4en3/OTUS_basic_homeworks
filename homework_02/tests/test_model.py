from unittest.mock import MagicMock
import pytest
from homework_02.mvc.model import Model
from homework_02.book import PhoneBook
from homework_02.resources.strings import FIELDS_MAP


@pytest.fixture
def setup_model():
    # Mock the data handler
    mock_data_handler = MagicMock()
    mock_data_handler.load_data_to_dict.return_value = {}
    mock_data_handler.save_data_to_file.return_value = True

    # Initialize model with mock data handler
    model = Model(mock_data_handler)
    model._Model__phonebook = PhoneBook()  # Inject an empty PhoneBook
    return model


def test_add_new_contact(setup_model):
    model = setup_model

    # Define a new contact's input data
    input_data = {
        FIELDS_MAP["FIELD_NAME"]: "John Doe",
        FIELDS_MAP["FIELD_PHONE"]: "81234567890",
        FIELDS_MAP["FIELD_COMMENT"]: "Friend",
    }

    # Call the method to add a new contact
    new_id = model.add_new_contact(input_data)

    # Assert that a valid ID was returned and the contact was added
    assert new_id == 1
    assert model.get_book().get_contact_by_id("1") is not None

    # Verify the contact's details
    contact = model.get_book().get_contact_by_id("1")
    assert contact.name == "John Doe"
    assert contact.phone == "81234567890"
    assert contact.comment == "Friend"
