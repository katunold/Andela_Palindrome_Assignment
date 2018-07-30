from unittest import TestCase
from palindrome import check_palindrome


class Tests(TestCase):
    def test_palindrome(self):
        self.assertEqual(check_palindrome("level"), "level is a Palindrome")
        self.assertEqual(check_palindrome(45), "45 is not a Palindrome")
        self.assertEqual(check_palindrome(44), "44 is a Palindrome")
        self.assertEqual(check_palindrome(" "), "You entered nothing")
