import pytest
from apps.numbers_app.app import get_pairs_of_numbers

test_data = [
    ("Positive test. Input in 10.", 10, 5),
    ("Negative test. Input is -10.", -10, 0),
    ("Negative test. Input is list.", [], 0)
]


@pytest.mark.parametrize('desc, input, expected', test_data, ids=[desc[0] for desc in test_data])
@pytest.mark.numbers
def test_get_pairs_of_numbers(desc, input, expected):
    actual = get_pairs_of_numbers(input)
    assert len(actual) == expected
