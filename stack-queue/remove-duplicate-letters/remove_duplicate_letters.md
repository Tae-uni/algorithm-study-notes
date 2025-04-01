# Remove Duplicate Letters (LeetCode #316)
Given a string `s`.  
Remove duplicate letters.  
Result is the smallest in lexicographical order.

**Constraints:**
> `1 <= s.length <= 10^4`  
> `s` consists of lowercase English letters.

ex1:  
Input: s = "bcabc"  
Output: "abc"

---

## Solution Approaches
### Approach 1: Stack
**Code:** [Remove Duplicate Letters - Stack](remove_duplicate_letters_stack.py)
```python
def removeDuplicateLetters(self, s: str) -> str:
    """
        counter(Counter): a counter to track the frequency.  
        seen(set): keeps track of characters already in the result.  
        stack(stack): store the characters of final result.
    """
    counter, seen, stack = collections.Counter(s), set(), []
    
    for char in s:
        counter[char] -= 1
        # If char exist in seen, move to next value.
        if char in seen:
            continue
            
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
            
        stack.append(char)
        seen.add(char)
        
    return ''.join(stack)
```

### Example Walkthrough
Input: `s = "cbacdcbc"`  
Counter: `{'c': 4, 'b': 2, 'a': 1, 'd': 1}`


>1. index 0, 'c':  
`counter['c'] -= 1` -> counter = {'c': 3, 'b': 2, 'a': 1, 'd': 1}  
`seen = {}` -> No 'c' in seen  
skip the while loop, empty stack.  
`stack = ['c']`, `seen = {'c'}`  
>2. index 1, 'b':  
`counter['b'] -= 1` -> counter = {'c': 3, 'b': 1, 'a': 1, 'd': 1}  
`seen = {'c'}` -> No 'b' in seen, so continue  
while loop,  
stack = ['c'], b < c and counter['c'] > 0 (There is 3 left 'c')  
-> remove the stack and the set, stack = [], seen = set()  
stack = ['b'], seen = {'b'}  
>3. index 2, 'a':  
`counter['a'] -= 1` -> counter = {'c': 3, 'b': 1, 'a': 0, 'd': 1}  
`seen = {'b'}` -> No 'b' in seen  
while loop,  
stack = ['b'], a < b and counter['b'] > 0 (There is 1 left 'b')  
-> remove the stack and the set, stack = [], seen = set()  
stack = ['a'], seen = {'a'}  
...

Final Stack: ['a', 'c', 'd', 'b']  
Return: "acdb"  


---

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Each character is pushed and popped from the stack at most once.  
- Space Complexity: `O(n)` Stack, `seen` set, and Counter all take up to `O(n)` space in the worst case.

---

### Approach 2: Recursive (Not Recommended)
**Code:** [Remove Duplicate Letters - Recursive](remove_duplicate_letters_recursive.py)
```python
def removeDuplicateLetters(self, s: str) -> str:
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        
        # If all characters in s still exist in the suffix.
        if set(s) == set(suffix):
            return char + self.removeDuplicateLetters(suffix.replace(char,''))
    
    return ''    # Base case: return empty string when 's' is empty.
```

### Example Walkthrough
**Concept:** The function selects the smallest letter. It ensures the substring starting. It removes that letter from the string and recurses.

Input: s = "cbacdcbc"  
Unique characters: set("cbacdcbc") -> `{'a', 'b', 'c', 'd'}`  
Sorted: sorted(set(s)) -> `['a', 'b', 'c', 'd']`  

>1. The first Recursive call (s = "cbacdcbc")  
'a':  
`s.index('a')` -> 2  
`suffix = s[2:]` -> "acdcbc"  
Check:  
`set(s)` is `{'a', 'b', 'c', 'd'}`  
`set("acdcbc")` is also `{'a', 'b', 'c', 'd'}`  
-> Condition satisfied.  
-> `'a'` is the first letter of result.  
Recursive Call.  
>```python
>self.removeDuplicateLetters("acdcbc".replace('a', ''))
>```
>"acdcbc".replace('a', '') -> "cdcbc"  
Therefore, the return value: "a" + removeDuplicateLetters("cdcbc") 
>
>2. The second Recursive Call (s = "cdcbc")  
Input: s = "cdcbc"  
Unique characters: set("cdcbc") -> `{'b', 'c', 'd'}`  
Sorted: sorted(set(s)) -> `['b', 'c', 'd']`
'b':  
`s.index('b')` -> 3  
`suffix = s[3:]` -> "bc"  
Check:  
`set(s)` is `{'b', 'c', 'd'}`  
`set("bc")` is `{'b', 'c'}`  
-> Condition failed.  
'c':  
`s.index('c')` -> 0  
`suffix = s[0:]` -> "cdcbc"  
Check:  
`set(s)` is `{'b', 'c', 'd'}`  
`set("cdcbc")` is `{'b', 'c', 'd'}`  
-> Condition satisfied.  
Choose 'c' as the next letter, and recursively call:  
>```python
>self.removeDuplicateLetters("cdcbc".replace('c', ''))
>```
>"cdcbc".replace('c', '') -> "db"  
Therefore, the return value: "c" + removeDuplicateLetters("db")  
...  
>
>**Base Case (s = "")**  
Input: s = ""  
The function returns "" immediately.
Final Result Combination  
> 4th call returns: "b"  
> 3rd call returns: "d" + "b" -> "db"
> 2nd call returns: "c" + "db" -> "cdb"
> 1st call returns: "a" + "cdb" -> "acdb"

Final Output: `"acdb"`

---

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n^2)` Each recursive call, `s.index(char)` and `suffix.replace()` take `O(n)`.  Also, recursion may occur up to `O(n)` times.
- Space Complexity: `O(n^2)` Due to recursive calls and string slicing/creating at each step.

---

## 🔥 Final Thoughts
Both approaches solve the `Remove Duplicate Letters` problem.  
Approach 1(stack-based) is more efficient and recommended way to solve the problem. It returns in `O(n)` time and uses linear space.  
Approach 2(recursive) is elegant and clean but less efficient due to repeated string and deep recursion.

The stack-based solution is optimal and widely used.  
Thus, the recursive approach is great for learning, but it does not scale well with larger inputs.

---

## References
[LeetCode #316](https://leetcode.com/problems/remove-duplicate-letters/)