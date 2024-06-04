import pytest
from services.csv_service import get_data_by_name, set_user_data, USER_DATA_CACHE


@pytest.fixture(scope="module", autouse=True)
def setup_user_data():
    # Sample data for testing
    USER_DATA_CACHE[('John', 'Doe')] = {
        'firstName': 'John',
        'lastName': 'Doe',
        'startTime': '08:00',
        'endTime': '17:00',
        'notes': 'Some notes',
        'program': 'Sample Program'
    }


def test_get_start_time():
    assert get_data_by_name('John', 'Doe', "startTime") == '08:00'


def test_get_end_time():
    assert get_data_by_name('John', 'Doe', "endTime") == '17:00'


def test_get_notes():
    assert get_data_by_name('John', 'Doe', "notes") == 'Some notes'


def test_get_program():
    assert get_data_by_name('John', 'Doe', "program") == 'Sample Program'


def test_set_program():
    set_user_data('John', 'Doe', 'program', 'Body good')
    assert get_data_by_name('John', 'Doe', "program") == 'Body good'
