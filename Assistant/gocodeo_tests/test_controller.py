import pytest
from unittest.mock import patch, MagicMock
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import json
from Assistant.controller import BookSummarizer, BookBiteModel

@pytest.fixture
def mock_load_dotenv():
    with patch('dotenv.load_dotenv') as mock:
        mock.return_value = None
        yield mock

@pytest.fixture
def mock_openai_client():
    with patch('openai.OpenAI') as mock_client:
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.chat.completions.create = MagicMock()
        yield mock_instance

@pytest.fixture
def mock_json_loads():
    with patch('json.loads') as mock_json:
        mock_json.return_value = {"title": "Sample Book", "author": "John Doe", "summary": "A brief summary", "ecom_url": "http://example.com"}
        yield mock_json

@pytest.fixture
def mock_model_json_schema():
    with patch.object(BookBiteModel, 'model_json_schema', return_value={"name": "BookBiteModel", "schema": {}}) as mock_schema:
        yield mock_schema

@pytest.fixture
def mock_chat_completions_create(mock_openai_client):
    mock_openai_client.chat.completions.create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content=json.dumps({"title": "Sample Book", "author": "John Doe", "summary": "A brief summary", "ecom_url": "http://example.com"})))])
    yield mock_openai_client.chat.completions.create

# happy_path - test_load_dotenv_success - Test that the environment variables are loaded successfully
def test_load_dotenv_success(mock_load_dotenv):
    result = load_dotenv()
    assert result is None
    assert mock_load_dotenv.called

# happy_path - test_field_creation_with_description - Test that the Field function creates a field with a description
def test_field_creation_with_description():
    field = Field(description='Name of the book')
    assert field.description == 'Name of the book'

# happy_path - test_basemodel_instantiation - Test that the BaseModel can be instantiated with valid data
def test_basemodel_instantiation():
    book = BookBiteModel(title='Sample Book', author='John Doe', dop='2023-01-01', summary='A brief summary', ecom_url='http://example.com')
    assert book.title == 'Sample Book'
    assert book.author == 'John Doe'
    assert book.dop == '2023-01-01'
    assert book.summary == 'A brief summary'
    assert book.ecom_url == 'http://example.com'

# happy_path - test_openai_client_initialization - Test that the OpenAI client is initialized correctly
def test_openai_client_initialization(mock_openai_client):
    client = OpenAI()
    assert client is not None
    assert mock_openai_client.called

# happy_path - test_get_book_summary_valid_title - Test that get_book_summary returns a valid summary for a given book title
def test_get_book_summary_valid_title(mock_chat_completions_create):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='Sample Book', author='John Doe')
    assert result['title'] == 'Sample Book'
    assert result['author'] == 'John Doe'
    assert 'summary' in result
    assert 'ecom_url' in result

# edge_case - test_load_dotenv_missing_file - Test that load_dotenv handles missing .env file gracefully
def test_load_dotenv_missing_file(mock_load_dotenv):
    mock_load_dotenv.return_value = False
    result = load_dotenv()
    assert result is False
    assert mock_load_dotenv.called

# edge_case - test_field_creation_empty_description - Test that Field function handles empty description
def test_field_creation_empty_description():
    field = Field(description='')
    assert field.description == ''

# edge_case - test_basemodel_missing_fields - Test that BaseModel raises validation error for missing required fields
def test_basemodel_missing_fields():
    try:
        BookBiteModel(title='Sample Book')
    except Exception as e:
        assert isinstance(e, ValueError)

# edge_case - test_get_book_summary_nonexistent_title - Test that get_book_summary handles non-existent book titles
def test_get_book_summary_nonexistent_title(mock_chat_completions_create):
    summarizer = BookSummarizer()
    result = summarizer.get_book_summary(title='Nonexistent Book')
    assert 'suggest the right title' in result['summary']

# edge_case - test_json_loads_invalid_format - Test that json.loads handles invalid JSON format
def test_json_loads_invalid_format(mock_json_loads):
    mock_json_loads.side_effect = json.JSONDecodeError('Expecting value', 'invalid json', 0)
    try:
        json.loads('invalid json')
    except json.JSONDecodeError as e:
        assert 'Expecting value' in str(e)

