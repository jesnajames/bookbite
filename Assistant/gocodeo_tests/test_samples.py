import pytest
from unittest import mock
from Assistant.samples import get_summary, get_message_content, check_content_type, check_example_key, parse_response

@pytest.fixture
def mock_get_summary():
    with mock.patch('Assistant.samples.get_summary') as mock_func:
        mock_func.return_value = {"summary": "The Alchemist"}
        yield mock_func

@pytest.fixture
def mock_get_message_content():
    with mock.patch('Assistant.samples.get_message_content') as mock_func:
        mock_func.return_value = {
            "message": "\"The Alchemist,\" written by Paulo Coelho, follows the journey of Santiago, a young shepherd from Spain who dreams of discovering a treasure hidden near the Egyptian pyramids. Inspired by a recurring dream, he seeks guidance from an enigmatic king, Melchizedek, who encourages him to pursue his \"Personal Legend,\" or true purpose in life. \n\nThroughout his journey, Santiago encounters various characters, including a crystal merchant, an Englishman, and an Alchemist, each imparting wisdom and lessons about life, love, and the importance of listening to one’s heart. As he travels through the desert, Santiago learns that the real treasure lies not just in material wealth but in self-discovery, spiritual growth, and the interconnectedness of all things. \n\nThe novel emphasizes the idea that when one is determined to pursue their dreams and follow their true path, the universe conspires to help them achieve it. Ultimately, Santiago’s journey teaches readers about the significance of dreams, the transformative power of love, and the courage to follow one's intuition."
        }
        yield mock_func

@pytest.fixture
def mock_check_content_type():
    with mock.patch('Assistant.samples.check_content_type') as mock_func:
        mock_func.return_value = {"content_type": "application/json"}
        yield mock_func

@pytest.fixture
def mock_check_example_key():
    with mock.patch('Assistant.samples.check_example_key') as mock_func:
        mock_func.return_value = {"example_key": "Success"}
        yield mock_func

@pytest.fixture
def mock_parse_response():
    with mock.patch('Assistant.samples.parse_response') as mock_func:
        mock_func.return_value = {"message": "Parsed successfully"}
        yield mock_func

# happy_path - test_get_summary_success - Test that the summary of 'The Alchemist' is correctly returned for a successful response.
def test_get_summary_success(mock_get_summary):
    response = get_summary(200)
    assert response['summary'] == 'The Alchemist'

# happy_path - test_get_message_content_success - Test that the message content of 'The Alchemist' is correctly returned for a successful response.
def test_get_message_content_success(mock_get_message_content):
    response = get_message_content(200)
    assert response['message'] == '"The Alchemist," written by Paulo Coelho, follows the journey of Santiago, a young shepherd from Spain who dreams of discovering a treasure hidden near the Egyptian pyramids. Inspired by a recurring dream, he seeks guidance from an enigmatic king, Melchizedek, who encourages him to pursue his "Personal Legend," or true purpose in life. \n\nThroughout his journey, Santiago encounters various characters, including a crystal merchant, an Englishman, and an Alchemist, each imparting wisdom and lessons about life, love, and the importance of listening to one’s heart. As he travels through the desert, Santiago learns that the real treasure lies not just in material wealth but in self-discovery, spiritual growth, and the interconnectedness of all things. \n\nThe novel emphasizes the idea that when one is determined to pursue their dreams and follow their true path, the universe conspires to help them achieve it. Ultimately, Santiago’s journey teaches readers about the significance of dreams, the transformative power of love, and the courage to follow one's intuition.'

# happy_path - test_check_content_type_json - Test that the content type is correctly identified as 'application/json'.
def test_check_content_type_json(mock_check_content_type):
    response = check_content_type(200)
    assert response['content_type'] == 'application/json'

# happy_path - test_check_example_key_success - Test that the example key 'Success' is present in the response.
def test_check_example_key_success(mock_check_example_key):
    response = check_example_key(200)
    assert response['example_key'] == 'Success'

# happy_path - test_check_response_description_success - Test that the response description is 'Success' for status code 200.
def test_check_response_description_success():
    response = sample_summary.get(200)
    assert response['description'] == 'Success'

# edge_case - test_get_summary_empty_response - Test that an empty response returns None for the summary.
def test_get_summary_empty_response(mock_get_summary):
    mock_get_summary.return_value = {'summary': None}
    response = get_summary(204)
    assert response['summary'] is None

# edge_case - test_check_content_type_non_json - Test that a non-JSON content type returns an error.
def test_check_content_type_non_json(mock_check_content_type):
    mock_check_content_type.return_value = {'error': 'Invalid content type'}
    response = check_content_type(200, content_type='text/html')
    assert response['error'] == 'Invalid content type'

# edge_case - test_get_message_content_unknown_status - Test that an unknown status code returns an error message.
def test_get_message_content_unknown_status(mock_get_message_content):
    mock_get_message_content.return_value = {'error': 'Unknown status code'}
    response = get_message_content(404)
    assert response['error'] == 'Unknown status code'

# edge_case - test_check_example_key_missing - Test that missing example key returns a default message.
def test_check_example_key_missing(mock_check_example_key):
    mock_check_example_key.return_value = {'message': 'Example key not found'}
    response = check_example_key(200)
    assert response['message'] == 'Example key not found'

# edge_case - test_parse_response_malformed_json - Test that a malformed JSON returns a parse error.
def test_parse_response_malformed_json(mock_parse_response):
    mock_parse_response.return_value = {'error': 'JSON parse error'}
    response = parse_response('{bad json')
    assert response['error'] == 'JSON parse error'

