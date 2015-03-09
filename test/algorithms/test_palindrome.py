from unittest import TestCase
from src.algorithms.palindrome import palindrome


class TestPalindrome(TestCase):
	def test_palindrome(self):
		self.assertFalse(palindrome(None))
		self.assertTrue(palindrome(8))
		self.assertTrue(palindrome("abba"))
		self.assertFalse(palindrome("abcabc"))
		self.assertTrue(palindrome("race car"))
		self.assertTrue(palindrome("kobyla ma maly bok"))
