# Valid Palindrome (LeetCode #125)

It doesn't matter if input is uppercase or lowercase letters and removing all non-alphanumeric cha.  
Palindrome: it reads the same forward and backward. Include letters & numbers.  

Given a string `s`, return `ture` if is a palindrome, or `false`.  
Constraints:
> 1 <= s.length <= 2 * 10^5

ex1:  
Input: s = "A man, a plan, a canal: Panama"  
Output: true  
Explanation: "amanaplanacanalpanama" is a palindrome.

## Solution Approaches

### Way 1: Using Slicing (`[::-1]`)
**Code:** [Slicing](valid_palindrome_slicing.py)

```python
def isPalindrome_slicing(s: str) -> bool:
    # (c.lower() for c in s if c.isalnum()) -> Generator expression.
    # string.join(iterable), takes all items in an iterable and join them into one string.
    s = ''.join(c.lower() for c in s if c.isalnum())

    # Check if the string is equal to revers.
    return s == s[::-1]
```

### Way 2: Using Two Pointers
**Code:** [Two Pointers](valid_palindrome_two_pointers.py)
```python
def isPalindrome_pointers(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right += 1
        
    return True
```

## Reference
[LeetCode Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)  
[.join](https://www.w3schools.com/python/ref_string_join.asp)