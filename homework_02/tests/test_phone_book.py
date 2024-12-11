def test_add_to_book(setup_phonebook_empty, setup_contact1):
    book = setup_phonebook_empty
    assert not book.add_to_book("String as a wrong object")
    assert book.add_to_book(setup_contact1)
    assert book.get_size() == 1
    assert book.get_contact_by_id(setup_contact1.id)


def test_delete_from_book(setup_phonebook_true, setup_contact1, setup_contact2, setup_contact3):
    book = setup_phonebook_true
    assert not book.delete_from_book("non_existing_id")
    assert book.delete_from_book(setup_contact1.id)
    assert book.get_size() == 2
    assert not book.get_contact_by_id(setup_contact1.id)
    assert book.get_contact_by_id(setup_contact2.id)
    assert book.get_contact_by_id(setup_contact3.id)


def test_get_book_as_dict(setup_phonebook_true, setup_phonebook_false1, setup_book_true_as_json,
                          setup_book_false_as_json):
    book = setup_phonebook_true
    assert book.get_book_as_dict() == setup_book_true_as_json

    book = setup_phonebook_false1
    assert book.get_book_as_dict() == setup_book_false_as_json


def test_is_empty(setup_phonebook_true, setup_phonebook_empty):
    book = setup_phonebook_true
    assert not book.is_empty()

    book = setup_phonebook_empty
    assert book.is_empty()


def test_get_max_id(setup_phonebook_true, setup_phonebook_empty, setup_contact3):
    book = setup_phonebook_true
    assert book.get_max_id() == 237
    book.delete_from_book(setup_contact3.id)
    assert book.get_max_id() == 236

    book = setup_phonebook_empty
    assert book.get_max_id() == 0


def test_get_contact_by_id(setup_phonebook_true, setup_contact1):
    book = setup_phonebook_true
    contact = book.get_contact_by_id(setup_contact1.id)
    assert contact.id == setup_contact1.id and contact.name == setup_contact1.name and contact.phone == setup_contact1.phone and contact.comment == setup_contact1.comment

    assert not book.get_contact_by_id("non_existing_id")


def test_get_book(setup_phonebook_true):
    book = setup_phonebook_true
    book_dict = book.get_book()
    assert isinstance(book_dict, dict)
    assert book_dict == book._PhoneBook__book
    assert book_dict == setup_phonebook_true._PhoneBook__book


def test_get_size(setup_phonebook_true, setup_phonebook_false1, setup_phonebook_empty):
    book = setup_phonebook_true
    assert book.get_size() == 3

    book = setup_phonebook_false1
    assert book.get_size() == 4

    book = setup_phonebook_empty
    assert book.get_size() == 0