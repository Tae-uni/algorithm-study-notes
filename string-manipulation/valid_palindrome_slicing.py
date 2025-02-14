def isPalindrome_slicing(s:str) -> bool:
    """
    Check the input if it's a palindrome.
    Uses generator expression for efficient(memory usage) processing.
    """
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]