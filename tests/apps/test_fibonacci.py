import pytest
from pbc.apps.fibonacci import get_fibonacci_sequence

test_data = [
    pytest.param(7, [0, 1, 1, 2, 3, 5, 8], id='Get fibonacci sequence up to 7.'),
    pytest.param(0, [], id='Input number is 0.'),
    pytest.param(-7, [], id='Input is -7.')
]


@pytest.mark.parametrize('input, expected', test_data)
@pytest.mark.fib
def test_get_fibonacci_sequence(input, expected):
    assert get_fibonacci_sequence(input) == expected
