import pytest
from apps.fibonacci_app.app import get_fibonacci_sequence


@pytest.mark.parametrize('case, input, expected', [
    ("Get fibonacci sequence up to 7.", 7, [0, 1, 1, 2, 3, 5, 8]),
    ("Input number is 0.", 0, []),
    ("Input is -7.", -7, [])
])
@pytest.mark.fib
def test_get_fibonacci_sequence(case, input, expected):
    print('\nCase: {}'.format(case))
    actual_list = get_fibonacci_sequence(input)
    assert actual_list == expected
    print('Passed.')
