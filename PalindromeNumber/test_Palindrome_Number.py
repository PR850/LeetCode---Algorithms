import pytest
from Palindrome_Number import isPalindrome

test_data = [
    (12345, False),
    (1, True),
    (121, True),
    (-1232, False),
    ('', False)
]


@pytest.mark.parametrize("test_input, expected_result", test_data)
def testIsPalindrome(test_input, expected_result):
    assert isPalindrome(test_input) == expected_result
