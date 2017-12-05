import pytest
from fibonacci import get_fibonacci_sequence


cases = [
    {
        "Case": "Get fibonacci sequence up to 7.",
        "input": 7,
        "expected": [0, 1, 1, 2, 3, 5, 8]
    },
    {
        "Case": "Input number is 0.",
        "input": 0,
        "expected": []
    },
    {
        "Case": "Input is -7.",
        "input": -7,
        "expected": []
    }
]


@pytest.fixture(params=cases)
def fibonacci_cases_fixture(request):
    return request.param


def test_get_fibonacci_sequence(fibonacci_cases_fixture):
    data = fibonacci_cases_fixture
    print('Case: {}'.format(data['Case']))
    actual_list = get_fibonacci_sequence(data['input'])
    assert actual_list == data['expected']
    print('Passed.')
