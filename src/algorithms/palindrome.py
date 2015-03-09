def palindrome(string):
	"""
	Tests if string is a palindrome.
	:param string: String to check.
	:return: True if string is palindrome, else otherwise.
	"""
	if string is None:
		return False

	s = str(string).replace(" ", "")

	i = 0
	while i <= len(s) - 1:
		if s[i] == s[len(s) - i - 1]:
			i += 1
			continue
		else:
			return False
	return True
