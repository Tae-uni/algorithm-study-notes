"""
    Both Solutions have same concept.
    The first solution is using Lexicographical Filtering `sorted(set(s))`.
    The second solution is using Minimal Position Sacn via linear iteration.
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ''
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            if s[i] not in s[i+1:]:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))