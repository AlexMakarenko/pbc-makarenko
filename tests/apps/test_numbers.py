import pytest
from pbc.apps.pairs_of_numbers import get_pairs_of_numbers

test_data = [
    pytest.param((1, 2, 3, 4, 5, 6, 7, 8, 9), 5, id='Positive test. Input is from 1 to 10.'),
    pytest.param((-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 5, id='Positive test. Input is from -3 to -10.'),
    pytest.param((2, 4, 6, 7, 3, 7, 5, 5, '', [], {}, 3.77, 6.33), 3,
                 id='Negative test. Input with string, dic, float, list.'),
    pytest.param([], 0, id='Negative test. Empty tuple.')
]


@pytest.mark.parametrize('input, expected', test_data)
@pytest.mark.numbers
def test_get_pairs_of_numbers(input, expected):
    assert len(get_pairs_of_numbers(*input)) == expected
