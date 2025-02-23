def longestPalindrome(s: str) -> str:
    """
        Using Two Pointer with Sliding Window approach.
        Expand window outward of palindrome, else move forward.
    """
    # Distinct palindrome & Expand two pointer.
    def expand(left:int, right:int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]

    # Exception Handling.
    if len(s) < 2 or s == s[::-1]:
        return s

    # Sliding window.
    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result