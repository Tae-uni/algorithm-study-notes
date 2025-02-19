# Reverse String (LeetCode #344)
A function that reverses a string.  
The input string is array of character s.  
> The input array must be modified **in-place** with **0(1)** extra memory.  

It means I cannot use `[::-1]` slicing here to reverse.

**Constraints:**
> 1 <= s.length <= 10^5  
> `s[i]` is a printable ascii character.

ex1:  
Input: s = ["h", "e", "l", "l", "o"]  
Output: ["o", "l", "l", "e", "h"]

---

## Solution Approaches
### Way 1: Two Pointers (Recommended)
**Code:** [Two Pointers](reverse_string.py) 

```python
def reverseString_two_pointer(s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    while right > left:
        # Switch the position.
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```
    
### Way 2: Simplified Two Pointers(`s[~i]`- *More Pythonic Way.*)
**Code:** [Pythonic Two Pointers](reverse_string_pythonic.py)

```python
def reverseString_simplified(s: List[str]) -> None:
    for i in range(len(s) // 2):
        # In Python, `~i` means bitwise Not.
        # `~i = -i - 1`. So, s[~i] = s[-(i+1)]
        s[i], s[~i] = s[~i], s[i]
```

### Way 3: Reverse the array. | *Not Recommend*
`s.reverse()`

---

## Final Thoughts
Way1 and 2 both use the two pointer approach. The difference is whether declare `left` and `right`, or just simply use the `~i` operator in Python.  
The `~i` operator make code simple, but it cannot be used in the other languages.  
Therefore, I considered the first way is the most suitable way to solve this problem. 

## References
- [LeetCode Reverse String](https://leetcode.com/problems/reverse-string/description/)  
- [Bitwise Not](https://www.geeksforgeeks.org/python-bitwise-operators/)