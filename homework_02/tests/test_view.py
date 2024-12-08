from unittest.mock import patch, MagicMock
from homework_02.mvc.view import View

def test_user_input():
    with patch("builtins.input", return_value="Test Input"):
        assert View.user_input("Enter something: ") == "test input"

def test_println(capsys):
    View.println("Hello, World!")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
