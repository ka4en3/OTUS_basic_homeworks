import json
from unittest.mock import patch, mock_open
from pytest import raises
from homework_02.mvc.json_handler import JSONHandler


def test_save_data_to_file(setup_book_true_as_json, setup_book_false_as_json,
                           setup_empty_json_file_for_tests):
    test_handler = JSONHandler(setup_empty_json_file_for_tests)

    assert test_handler.save_data_to_file(setup_book_true_as_json), "The save operation did not return True."
    with open(setup_empty_json_file_for_tests, encoding="UTF-8") as file:
        data = json.load(file)
    assert data == setup_book_true_as_json, "The saved data does not match the expected output."

    assert test_handler.save_data_to_file(setup_book_false_as_json), "The save operation did not return True."
    with open(setup_empty_json_file_for_tests, encoding="UTF-8") as file:
        data = json.load(file)
    assert data == setup_book_false_as_json, "The saved data does not match the expected output."


def test_load_data_to_dict(setup_json_file_with_data_for_tests, setup_json_file_with_wrong_data_for_tests,
                           setup_book_true_as_json):
    test_handler = JSONHandler(setup_json_file_with_data_for_tests)
    data = test_handler.load_data_to_dict()
    assert data == setup_book_true_as_json, "The loaded data does not match the expected output."

    test_handler = JSONHandler("not existing path")
    data = test_handler.load_data_to_dict()
    assert data == {}, "Loading non-existing file should return an empty dictionary."

    # Use pytest.raises to check for the expected exception
    test_handler = JSONHandler(setup_json_file_with_wrong_data_for_tests)
    with raises(json.JSONDecodeError):
        test_handler.load_data_to_dict()


def test_load_data_to_dict_handles_malformed_json():
    with raises(json.JSONDecodeError):
        with patch("os.path.exists", return_value=True):
            # Mock open to provide malformed JSON content
            malformed_json = "{malformed_json: true}"  # Invalid JSON syntax
            with patch("builtins.open", mock_open(read_data=malformed_json)):
                with patch("json.load", side_effect=json.JSONDecodeError("JSON decoding error!", "document for example",
                                                                         0)):  # Simulate JSON decoding error
                    test_handler = JSONHandler("malformed.json")
                    test_handler.load_data_to_dict()
