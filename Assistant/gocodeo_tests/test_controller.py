import pytest
from unittest.mock import patch, MagicMock
from openai import OpenAI
from Assistant.controller import BookBiteModel, BookSummarizer
import json

@pytest.fixture
def mock_openai():
    with patch('Assistant.controller.OpenAI') as mock:
        mock_instance = mock.return_value
        mock_instance.chat.completions.create = MagicMock(return_value=MagicMock(
            choices=[MagicMock(message=MagicMock(content=json.dumps({
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "summary": "A summary of the book",
                "dop": "1925-04-10",
                "ecom_url": "http://example.com"
            })))]
        ))
        yield mock_instance

@pytest.fixture
def book_summarizer(mock_openai):
    return BookSummarizer()

@pytest.fixture
def book_bite_model():
    return BookBiteModel(title="The Great Gatsby", author="F. Scott Fitzgerald", dop="1925-04-10", summary="A summary of the book", ecom_url="http://example.com")

def test_get_book_summary_valid_title_author(book_summarizer, mock_openai, book_bite_model):
    result = book_summarizer.get_book_summary(title='The Great Gatsby', author='F. Scott Fitzgerald')
    assert result['title'] == 'The Great Gatsby'
    assert result['author'] == 'F. Scott Fitzgerald'

# happy_path - test_get_book_summary_valid_title_no_author - Test that get_book_summary returns a valid BookBiteModel with correct title and no author
def test_get_book_summary_valid_title_no_author(book_summarizer, mock_openai, book_bite_model):
    mock_openai.chat.completions.create.return_value.choices[0].message.content = json.dumps(book_bite_model.model_dump())
    result = book_summarizer.get_book_summary(title='1984')
    assert result['title'] == '1984'

# happy_path - test_get_book_summary_imaginary_title - Test that get_book_summary handles imaginary title and suggests correct one
def test_get_book_summary_imaginary_title(book_summarizer, mock_openai):
    mock_openai.chat.completions.create.return_value.choices[0].message.content = json.dumps({'summary': 'suggest the right title'})
    result = book_summarizer.get_book_summary(title='The Imaginary Book')
    assert 'suggest the right title' in result['summary']

# happy_path - test_get_book_summary_special_characters - Test that get_book_summary returns a valid BookBiteModel with special characters in title
def test_get_book_summary_special_characters(book_summarizer, mock_openai, book_bite_model):
    mock_openai.chat.completions.create.return_value.choices[0].message.content = json.dumps(book_bite_model.model_dump())
    result = book_summarizer.get_book_summary(title="Harry Potter & The Philosopher's Stone")
    assert result['title'] == "Harry Potter & The Philosopher's Stone"

# happy_path - test_get_book_summary_long_title - Test that get_book_summary returns a valid BookBiteModel with long title
def test_get_book_summary_long_title(book_summarizer, mock_openai, book_bite_model):
    mock_openai.chat.completions.create.return_value.choices[0].message.content = json.dumps(book_bite_model.model_dump())
    result = book_summarizer.get_book_summary(title="The Hitchhiker's Guide to the Galaxy: A Trilogy in Four Parts")
    assert result['title'] == "The Hitchhiker's Guide to the Galaxy: A Trilogy in Four Parts"

# edge_case - test_get_book_summary_empty_title - Test that get_book_summary handles empty title gracefully
def test_get_book_summary_empty_title(book_summarizer, mock_openai):
    mock_openai.chat.completions.create.return_value.choices[0].message.content = json.dumps({'summary': 'request them to check the title once again'})
    result = book_summarizer.get_book_summary(title='')
    assert 'request them to check the title once again' in result['summary']

# edge_case - test_get_book_summary_non_existent_author - Test that get_book_summary handles non-existent author gracefully
def test_get_book_summary_non_existent_author(book_summarizer, mock_openai, book_bite_model):
    mock_openai.chat.completions.create.return_value.choices[0].message.content = json.dumps(book_bite_model.model_dump())
    result = book_summarizer.get_book_summary(title='War and Peace', author='Unknown Author')
    assert result['title'] == 'War and Peace'

# edge_case - test_get_book_summary_null_title - Test that get_book_summary handles null title input
def test_get_book_summary_null_title(book_summarizer, mock_openai):
    mock_openai.chat.completions.create.return_value.choices[0].message.content = json.dumps({'summary': 'request them to check the title once again'})
    result = book_summarizer.get_book_summary(title=None)
    assert 'request them to check the title once again' in result['summary']

# edge_case - test_get_book_summary_numeric_title - Test that get_book_summary handles numeric title input
def test_get_book_summary_numeric_title(book_summarizer, mock_openai):
    mock_openai.chat.completions.create.return_value.choices[0].message.content = json.dumps({'summary': 'suggest the right title'})
    result = book_summarizer.get_book_summary(title='12345')
    assert 'suggest the right title' in result['summary']

# edge_case - test_get_book_summary_long_author_name - Test that get_book_summary handles extremely long author name
def test_get_book_summary_long_author_name(book_summarizer, mock_openai, book_bite_model):
    mock_openai.chat.completions.create.return_value.choices[0].message.content = json.dumps(book_bite_model.model_dump())
    result = book_summarizer.get_book_summary(title='The Odyssey', author='Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer Homer')
    assert result['title'] == 'The Odyssey'

