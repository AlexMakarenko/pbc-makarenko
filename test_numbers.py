import pytest
from numbers import get_pairs_of_numbers


cases = [
    {
        "Case": "Positive test.",
        "expected": {(4, 6), (5, 5), (2, 8), (1, 9), (3, 7)}
    }
]


@pytest.fixture(params=cases)
def cases_for_numbers_fixture(request):
    return request.param


def test_get_pairs_of_numbers(cases_for_numbers_fixture):
    data = cases_for_numbers_fixture
    print('Case: {}'.format(data['Case']))
    actual = get_pairs_of_numbers()
    assert actual == data['expected']
    print('Passed.')