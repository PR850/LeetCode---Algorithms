import pytest
from Reverse_integer import reverse

test_data = [
    (321, 123),
    (1, 1),
    (-321, -123),
    (0, 0)
]


@pytest.mark.parametrize("test_input, expected_result", test_data)
def testReverse(test_input, expected_result):
    assert reverse(test_input) == expected_result
