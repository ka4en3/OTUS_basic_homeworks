def test_load_data_to_dict():
    pass

def test_save_data_to_file(setup_json_handler_save_to_file, setup_book_true_as_json):
    test_handler = setup_json_handler_save_to_file
    test_handler.save_data_to_file(setup_book_true_as_json)