import pytest
from unittest.mock import patch, MagicMock
from Assistant.controller import BookBiteModel, BookSummarizer

@pytest.fixture
def mock_openai_client():
    with patch('Assistant.controller.OpenAI') as mock:
        mock_instance = MagicMock()
        mock.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content='{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "dop": "1925", "summary": "A novel about the American dream and the roaring twenties, centered on the mysterious Jay Gatsby.", "ecom_url": "https://www.amazon.com/great-gatsby"}'))]
        )
        yield mock_instance

@pytest.fixture(autouse=True)
def mock_load_dotenv():
    with patch('Assistant.controller.load_dotenv') as mock:
        yield mock

@pytest.fixture
def mock_book_bite_model():
    with patch('Assistant.controller.BookBiteModel') as mock:
        yield mock

# happy path - get_book_summary - Test that get_book_summary returns a valid summary for a given title and author
def test_get_book_summary_with_title_and_author(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='The Great Gatsby', author='F. Scott Fitzgerald')
    expected = {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'dop': '1925',
        'summary': 'A novel about the American dream and the roaring twenties, centered on the mysterious Jay Gatsby.',
        'ecom_url': 'https://www.amazon.com/great-gatsby'
    }
    assert result == expected


# happy path - get_book_summary - Test that get_book_summary returns a valid summary for a given title without author
def test_get_book_summary_with_title_only(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='1984')
    expected = {
        'title': '1984',
        'author': 'George Orwell',
        'dop': '1949',
        'summary': 'A dystopian novel set in a totalitarian society under constant surveillance.',
        'ecom_url': 'https://www.amazon.com/1984'
    }
    assert result == expected


# happy path - get_book_summary - Test that get_book_summary handles a title with special characters
def test_get_book_summary_with_special_characters(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title="Harry Potter & the Philosopher's Stone")
    expected = {
        'title': "Harry Potter and the Philosopher's Stone",
        'author': 'J.K. Rowling',
        'dop': '1997',
        'summary': 'A young boy discovers he is a wizard and attends Hogwarts School of Witchcraft and Wizardry.',
        'ecom_url': 'https://www.amazon.com/harry-potter-philosophers-stone'
    }
    assert result == expected


# happy path - get_book_summary - Test that get_book_summary returns correct data for a well-known book
def test_get_book_summary_well_known(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='To Kill a Mockingbird', author='Harper Lee')
    expected = {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'dop': '1960',
        'summary': 'A story of racial injustice and childhood in the Deep South.',
        'ecom_url': 'https://www.amazon.com/to-kill-a-mockingbird'
    }
    assert result == expected


# happy path - get_book_summary - Test that get_book_summary suggests correct title for an imaginary book
def test_get_book_summary_imaginary_title(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='The Adventures of Frodo')
    expected = {
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'dop': '1954',
        'summary': 'An epic fantasy adventure about the quest to destroy the One Ring.',
        'ecom_url': 'https://www.amazon.com/lord-of-the-rings'
    }
    assert result == expected


# edge case - get_book_summary - Test that get_book_summary handles empty title input gracefully
def test_get_book_summary_empty_title(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='')
    expected = {'error': 'Title cannot be empty'}
    assert result == expected


# edge case - get_book_summary - Test that get_book_summary handles non-existent book title
def test_get_book_summary_non_existent_title(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='A Book That Does Not Exist')
    expected = {'error': 'No summary available for the given title'}
    assert result == expected


# edge case - get_book_summary - Test that get_book_summary handles very long book titles
def test_get_book_summary_long_title(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='A Very Long Book Title That Exceeds Normal Lengths')
    expected = {'error': 'Title is too long to process'}
    assert result == expected


# edge case - get_book_summary - Test that get_book_summary handles special characters in author name
def test_get_book_summary_special_author_name(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='The Alchemist', author='Paulo Coelho!')
    expected = {
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'dop': '1988',
        'summary': 'A fable about following your dream.',
        'ecom_url': 'https://www.amazon.com/the-alchemist'
    }
    assert result == expected


# edge case - get_book_summary - Test that get_book_summary handles missing author field
def test_get_book_summary_missing_author(mock_openai_client):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='Brave New World')
    expected = {
        'title': 'Brave New World',
        'author': 'Aldous Huxley',
        'dop': '1932',
        'summary': 'A dystopian novel about a technologically advanced future society.',
        'ecom_url': 'https://www.amazon.com/brave-new-world'
    }
    assert result == expected


