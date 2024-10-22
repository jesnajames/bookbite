import pytest
from unittest import mock
from Assistant.samples import get_summary, get_message_content, get_content_type, get_description, get_example_key

@pytest.fixture
def mock_get_summary():
    with mock.patch('Assistant.samples.get_summary') as mock_summary:
        mock_summary.return_value = {
            'summary': 'The Alchemist'
        }
        yield mock_summary

@pytest.fixture
def mock_get_message_content():
    with mock.patch('Assistant.samples.get_message_content') as mock_message_content:
        mock_message_content.return_value = {
            'message': {
                'summary': '"The Alchemist," written by Paulo Coelho, follows the journey of Santiago, a young shepherd from Spain who dreams of discovering a treasure hidden near the Egyptian pyramids. Inspired by a recurring dream, he seeks guidance from an enigmatic king, Melchizedek, who encourages him to pursue his "Personal Legend," or true purpose in life. \n\nThroughout his journey, Santiago encounters various characters, including a crystal merchant, an Englishman, and an Alchemist, each imparting wisdom and lessons about life, love, and the importance of listening to one’s heart. As he travels through the desert, Santiago learns that the real treasure lies not just in material wealth but in self-discovery, spiritual growth, and the interconnectedness of all things. \n\nThe novel emphasizes the idea that when one is determined to pursue their dreams and follow their true path, the universe conspires to help them achieve it. Ultimately, Santiago’s journey teaches readers about the significance of dreams, the transformative power of love, and the courage to follow one\'s intuition.'
            }
        }
        yield mock_message_content

@pytest.fixture
def mock_get_content_type():
    with mock.patch('Assistant.samples.get_content_type') as mock_content_type:
        mock_content_type.return_value = {
            'content_type': 'application/json'
        }
        yield mock_content_type

@pytest.fixture
def mock_get_description():
    with mock.patch('Assistant.samples.get_description') as mock_description:
        mock_description.return_value = {
            'description': 'Success'
        }
        yield mock_description

@pytest.fixture
def mock_get_example_key():
    with mock.patch('Assistant.samples.get_example_key') as mock_example_key:
        mock_example_key.return_value = {
            'example_key': 'Success'
        }
        yield mock_example_key

# happy path - get_summary - Test that the summary is correctly retrieved for status code 200
def test_summary_retrieval_200(mock_get_summary):
    result = get_summary(200)
    assert result['summary'] == 'The Alchemist'


# happy path - get_message_content - Test that the message content is correctly retrieved for status code 200
def test_message_content_200(mock_get_message_content):
    result = get_message_content(200)
    expected_summary = '"The Alchemist," written by Paulo Coelho, follows the journey of Santiago, a young shepherd from Spain who dreams of discovering a treasure hidden near the Egyptian pyramids. Inspired by a recurring dream, he seeks guidance from an enigmatic king, Melchizedek, who encourages him to pursue his "Personal Legend," or true purpose in life. \n\nThroughout his journey, Santiago encounters various characters, including a crystal merchant, an Englishman, and an Alchemist, each imparting wisdom and lessons about life, love, and the importance of listening to one’s heart. As he travels through the desert, Santiago learns that the real treasure lies not just in material wealth but in self-discovery, spiritual growth, and the interconnectedness of all things. \n\nThe novel emphasizes the idea that when one is determined to pursue their dreams and follow their true path, the universe conspires to help them achieve it. Ultimately, Santiago’s journey teaches readers about the significance of dreams, the transformative power of love, and the courage to follow one\'s intuition.'
    assert result['message']['summary'] == expected_summary


# happy path - get_content_type - Test that the response content type is application/json for status code 200
def test_content_type_200(mock_get_content_type):
    result = get_content_type(200)
    assert result['content_type'] == 'application/json'


# happy path - get_description - Test that the description is 'Success' for status code 200
def test_description_200(mock_get_description):
    result = get_description(200)
    assert result['description'] == 'Success'


# happy path - get_example_key - Test that the example key 'Success' is present for status code 200
def test_example_key_200(mock_get_example_key):
    result = get_example_key(200)
    assert result['example_key'] == 'Success'


# edge case - get_summary - Test that an empty response is handled gracefully for non-existing status code
def test_summary_retrieval_non_existing():
    with mock.patch('Assistant.samples.get_summary', return_value={'summary': None}):
        result = get_summary(404)
        assert result['summary'] is None


# edge case - get_content_type - Test that an invalid content type is handled gracefully
def test_invalid_content_type():
    with mock.patch('Assistant.samples.get_content_type', return_value={'content_type': None}):
        result = get_content_type(500)
        assert result['content_type'] is None


# edge case - get_description - Test that missing description is handled for non-existing status code
def test_missing_description_non_existing():
    with mock.patch('Assistant.samples.get_description', return_value={'description': None}):
        result = get_description(404)
        assert result['description'] is None


# edge case - get_example_key - Test that missing example key is handled for non-existing status code
def test_missing_example_key_non_existing():
    with mock.patch('Assistant.samples.get_example_key', return_value={'example_key': None}):
        result = get_example_key(404)
        assert result['example_key'] is None


# edge case - get_message_content - Test that malformed JSON is handled gracefully
def test_malformed_json_handling():
    with mock.patch('Assistant.samples.get_message_content', return_value={'message': None}):
        result = get_message_content(501)
        assert result['message'] is None


