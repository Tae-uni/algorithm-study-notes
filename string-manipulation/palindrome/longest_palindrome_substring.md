# Longest Palindromic Substring (LeetCode #5)

Given a string `s`,  
Return the longest palindromic substring in `s`.

There are two types of palindromes.  
Odd palindrome: `"aba"`, `"racecar"`  
Even palindrome: `"abba"`, `"noon"`

Constraints:  
> 1 <= s.length <= 1000  
> `s` is only digits and English letters.

ex1:  
Input: s = "babad"  
Output: "bab"  
Explanation: "aba" is also a valid answer.


## Solution Approaches
### Way 1: TwoPointer with Sliding Window

**Code:** [Longest Palindrome - Slicing](longest_palindrome_slicing.py)
```python
def longestPalindrome(s: str) -> str:
    # left and right are pointer that expand both side.
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right -= 1
        """
            When the loop ends, the palindrome cannot expand anymore.
            At that moment, left and right are already out of the palindrome.
            Therefore, it needs left + 1, right.
        """
        # Slicing s[0:3] returns 0,1,2.
        return s[left+1 : right]
    
    # Exception Handling: Make the code more efficient.
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    
    for i in range(len(s) - 1):
        # Checks both even and odd length palindromes.
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result
```
#### ⏳ Time & Space Complexity
- Time Complexity: `O(n^2)` Expanding each center takes `O(n)`, iterating over all `n` indices.
- Space Complexity: `O(n)` Stores substrings for comparison.

### Way 2: 
**Code:** [Longest Palindrome - Expand](longest_palindrome_expand.py)
```python
def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    
    def expand_around_center(s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of `s`.
        return right - left - 1

    start = 0
    end = 0

    """
        Find the actual location of longest length with def expand_around_center.
        Treating the `i` as a potential center, and expand around index `i`. 
    """
    for i in range(len(s)):
        # Odd length palindrome (center is a single character; ex: 'dad')
        odd = expand_around_center(s, i, i)
        # Even length palindrome (center is between two characters; ex: 'abba')
        even = expand_around_center(s, i, i + 1)
        max_len = max(odd, even)

        # If the current palindrome is longer than previous one, update the value.
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start : end+1]
```

#### ⏳Time & Space Complexity
- Time Complexity: `O(n^2)` Each character is considered as a center, expanding takes `O(n)`.  
- Space Complexity: `O(1)` Only uses **start, end** indices, no extra storage.  

## 🔥 Final Thoughts
Both approaches follow the same core idea.
> Using Two Pointer with Sliding Window approach.  
> Two Pointers (left, right) define the window boundaries.  
> Expand the window outward if it's a palindrome. Otherwise, move the window forward.

Way 1: Simple and easy to implement with Python's functions. But, higher memory usage `O(n)` due to substring slicing.  
Way 2: More optimized `O(1)` space, it only tracks indices. But, requires additional index calculations.

Way 2 is preferred for better performance`O(1)`. However, Way 1 is more readable and simpler. So both approaches are valid choices.

## Reference
[LeetCode #5](https://leetcode.com/problems/longest-palindromic-substring/description/)