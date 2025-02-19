from typing import List

""" 
Classic way to approach the reverse string problem.
Using Two Pointer, and switch the position at the end.
"""
def reverseString(s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    while right > left:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1