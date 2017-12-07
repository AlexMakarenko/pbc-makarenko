import pytest
from apps.numbers_app.app import get_pairs_of_numbers

test_data = [
    pytest.param(10, 5, id='Positive test. Input in 10.'),
    pytest.param(-10, 0, id='Negative test. Input is -10.'),
    pytest.param([], 0, id='Negative test. Input is list.')
]


@pytest.mark.parametrize('input, expected', test_data)
@pytest.mark.numbers
def test_get_pairs_of_numbers(input, expected):
    actual = get_pairs_of_numbers(input)
    assert len(actual) == expected
