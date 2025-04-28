import pytest
from unittest.mock import patch, MagicMock
from Assistant.controller import BookBiteModel, BookSummarizer

@pytest.fixture
def mock_openai_client():
    with patch('Assistant.controller.OpenAI') as mock:
        mock_instance = MagicMock()
        mock.chat.completions.create = MagicMock(return_value=MagicMock(choices=[MagicMock(message=MagicMock(content=json.dumps({
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "dop": "1925",
            "summary": "A novel about the American dream and the roaring twenties, centered around the mysterious Jay Gatsby.",
            "ecom_url": "https://www.amazon.com/great-gatsby"
        })))]))
        yield mock_instance

@pytest.fixture
def mock_load_dotenv():
    with patch('Assistant.controller.load_dotenv') as mock:
        yield mock

@pytest.fixture
def mock_json_loads():
    with patch('json.loads') as mock:
        yield mock

# happy path - get_book_summary - Test that valid book title and author returns correct summary
def test_valid_title_and_author(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='The Great Gatsby', author='F. Scott Fitzgerald')
    expected = {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "dop": "1925",
        "summary": "A novel about the American dream and the roaring twenties, centered around the mysterious Jay Gatsby.",
        "ecom_url": "https://www.amazon.com/great-gatsby"
    }
    assert result == expected


# happy path - get_book_summary - Test that valid book title without author returns correct summary
def test_valid_title_without_author(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='1984')
    expected = {
        "title": "1984",
        "author": "George Orwell",
        "dop": "1949",
        "summary": "A dystopian novel set in a totalitarian society under constant surveillance.",
        "ecom_url": "https://www.amazon.com/1984"
    }
    assert result == expected


# happy path - get_book_summary - Test that valid book title with different case returns correct summary
def test_title_with_different_case(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='to kill a mockingbird')
    expected = {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "dop": "1960",
        "summary": "A novel about racial injustice in the Deep South, seen through the eyes of a young girl.",
        "ecom_url": "https://www.amazon.com/to-kill-a-mockingbird"
    }
    assert result == expected


# happy path - get_book_summary - Test that valid book title with leading/trailing spaces returns correct summary
def test_title_with_spaces(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='  Brave New World  ')
    expected = {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "dop": "1932",
        "summary": "A dystopian novel about a future society driven by technological advancement and consumerism.",
        "ecom_url": "https://www.amazon.com/brave-new-world"
    }
    assert result == expected


# happy path - get_book_summary - Test that valid book title with special characters returns correct summary
def test_title_with_special_characters(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title="Harry Potter & the Philosopher's Stone")
    expected = {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "dop": "1997",
        "summary": "A young wizard's journey begins as he attends Hogwarts School of Witchcraft and Wizardry.",
        "ecom_url": "https://www.amazon.com/harry-potter-philosophers-stone"
    }
    assert result == expected


# edge case - get_book_summary - Test that non-existent book title suggests checking the title
def test_non_existent_title(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='The Invisible Unicorn')
    expected = {
        "title": "",
        "author": "",
        "dop": "",
        "summary": "The title may be imaginary. Please check the title and try again.",
        "ecom_url": ""
    }
    assert result == expected


# edge case - get_book_summary - Test that empty book title returns error message
def test_empty_title(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='')
    expected = {
        "title": "",
        "author": "",
        "dop": "",
        "summary": "The title may be imaginary. Please check the title and try again.",
        "ecom_url": ""
    }
    assert result == expected


# edge case - get_book_summary - Test that numeric book title is handled properly
def test_numeric_title(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='123456')
    expected = {
        "title": "",
        "author": "",
        "dop": "",
        "summary": "The title may be imaginary. Please check the title and try again.",
        "ecom_url": ""
    }
    assert result == expected


# edge case - get_book_summary - Test that book title with only special characters is handled properly
def test_special_characters_only_title(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='@#$%^&*')
    expected = {
        "title": "",
        "author": "",
        "dop": "",
        "summary": "The title may be imaginary. Please check the title and try again.",
        "ecom_url": ""
    }
    assert result == expected


# edge case - get_book_summary - Test that extremely long book title is handled properly
def test_extremely_long_title(mock_openai_client, mock_load_dotenv, mock_json_loads):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='A very long book title that exceeds normal length expectations and should be handled properly by the system')
    expected = {
        "title": "",
        "author": "",
        "dop": "",
        "summary": "The title may be imaginary. Please check the title and try again.",
        "ecom_url": ""
    }
    assert result == expected


