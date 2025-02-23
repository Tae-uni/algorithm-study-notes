def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    # Find the longest length.
    def expand_around_center(s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length.
        return right - left - 1

    start = 0
    end = 0

    # Find the actual location of longest length.
    for i in range(len(s)):
        odd = expand_around_center(s, i, i)
        even = expand_around_center(s, i, i + 1)
        max_len = max(odd, even)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end+1]