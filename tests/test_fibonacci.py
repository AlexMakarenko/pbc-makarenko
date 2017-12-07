import pytest
from apps.fibonacci_app.app import get_fibonacci_sequence

test_data = [
    ("Get fibonacci sequence up to 7.", 7, [0, 1, 1, 2, 3, 5, 8]),
    ("Input number is 0.", 0, []),
    ("Input is -7.", -7, [])
]


@pytest.mark.parametrize('desc, input, expected', test_data, ids=[desc[0] for desc in test_data])
@pytest.mark.fib
def test_get_fibonacci_sequence(desc, input, expected):
    actual_list = get_fibonacci_sequence(input)
    assert actual_list == expected
