import pytest
from unittest import mock
from fastapi.testclient import TestClient
from app import app
from Assistant.controller import BookSummarizer
from Assistant.samples import sample_summary

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def mock_book_summarizer():
    with mock.patch('Assistant.controller.BookSummarizer.get_book_summary') as mock_get_summary:
        yield mock_get_summary

@pytest.fixture
def mock_sample_summary():
    with mock.patch('Assistant.samples.sample_summary') as mock_sample:
        yield mock_sample

@pytest.fixture
def mock_uvicorn_run():
    with mock.patch('uvicorn.run') as mock_run:
        yield mock_run

# happy path - home - Test that the home endpoint returns a welcome message
def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello there! How can I help?'}


# happy path - summary_request - Test that the summarize endpoint returns a summary with only title provided
def test_summary_request_with_title(client, mock_book_summarizer):
    mock_book_summarizer.return_value = {'summary': 'Sample summary text'}
    response = client.get('/summarize?title=The+Great+Gatsby')
    assert response.status_code == 200
    assert response.json() == {'summary': 'Sample summary text'}


# happy path - summary_request - Test that the summarize endpoint returns a summary with title and author provided
def test_summary_request_with_title_and_author(client, mock_book_summarizer):
    mock_book_summarizer.return_value = {'summary': 'Sample summary text'}
    response = client.get('/summarize?title=The+Great+Gatsby&author=F.+Scott+Fitzgerald')
    assert response.status_code == 200
    assert response.json() == {'summary': 'Sample summary text'}


# edge case - summary_request - Test that the summarize endpoint handles non-existent book title gracefully
def test_summary_request_non_existent_title(client, mock_book_summarizer):
    mock_book_summarizer.return_value = {'error': 'Book not found'}
    response = client.get('/summarize?title=Non+Existent+Book')
    assert response.status_code == 200
    assert response.json() == {'error': 'Book not found'}


# edge case - summary_request - Test that the summarize endpoint handles empty title input
def test_summary_request_empty_title(client, mock_book_summarizer):
    mock_book_summarizer.return_value = {'error': 'Title is required'}
    response = client.get('/summarize?title=')
    assert response.status_code == 200
    assert response.json() == {'error': 'Title is required'}


# edge case - summary_request - Test that the summarize endpoint handles long title input
def test_summary_request_long_title(client, mock_book_summarizer):
    mock_book_summarizer.return_value = {'summary': 'Sample summary text'}
    response = client.get('/summarize?title=A+very+long+book+title+that+exceeds+typical+length')
    assert response.status_code == 200
    assert response.json() == {'summary': 'Sample summary text'}


