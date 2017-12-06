import pytest
from apps.numbers_app.app import get_pairs_of_numbers


@pytest.mark.parametrize('case, input, expected', [
    ("Positive test. Input in 10.", 10, 5),
    ("Negative test. Input is -10.", -10, 0),
    ("Negative test. Input is list.", [], 0)
])
@pytest.mark.numbers
def test_get_pairs_of_numbers(case, input, expected):
    print('\nCase: {}'.format(case))
    actual = get_pairs_of_numbers(input)
    assert len(actual) == expected
    print('Passed.')
