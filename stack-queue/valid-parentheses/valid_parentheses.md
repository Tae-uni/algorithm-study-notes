# Valid Parentheses (LeetCode #20)

Given a string `s`. Containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`.  
Determine if the input string is valid.  

Conditions of valid:  
1. Open brackets must be closed by the same type of brackets.  
2. Must be closed in the correct order.  
3. Every close bracket has a corresponding open bracket of the same type.

**Constraints:**
> 1 <= s.length <= 10^4  
> `s` consists of parentheses only `'()[]{}'`.


ex1:  
Input: s = "( )"  
Output: true  

ex2:  
Input: s = "( ]"  
Output: False

---

## Solution Approaches
### Approach 1: Hashmap (Dictionary)
**Code:** [Valid Parentheses - Hashmap](valid_parentheses_hashmap.py)
```python
def isValid(self, s: str) -> bool:
    # Initialize an empty stack to track open brackets.
    stack = []
    
    # Mapping of closing brackets to their opening brackets. Hash map & Dictionary.
    table = {
        ')': '(',
        '{': '}',
        '[': ']',
    }
    
    for char in s:
        if char in table:
            # If it is a closing bracket:
            # Check if stack is not empty, and top of the stack matches expected opening bracket`({[`.
            if stack and stack[-1] == table[char]:
                stack.pop() # Valid pair found, remove from stack.
            else:
                return False # Stack is empty or mismatch: Invalid(False).
        
        # If it is an opening bracket, push to the stack.
        else:
            stack.append(char)
    
    # If stack is empty, all brackets were matched.
    # return len(stack) == 0
    return not stack
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Each character is processed once in a single pass through the string.
- Space Complexity: `O(n)` In the worst case, all opening brackets are stored in stack.

---

### Approach 2: Manual Check
**Code:** [Valid Parentheses - Manual Check](valid_parentheses_manual_check.py)
```python
def isValid(self, s: str) -> bool:
    stack = []

    for i in range(len(s)):
        if stack:
            last = stack[-1]    # Get the last opened bracket.
            if self.is_pair(last, s[i]):    # Check if current is matching close.
                stack.pop()
                continue
        stack.append(s[i])    # Push open bracket or unmatched closing.

    return not stack

def is_pair(self, last, curr):
    if last == "(" and curr == ")" or last == "{" and curr == "}" or last == "[" and curr == "]":
        return True
    return False
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Iterates through the input string once.
- Space Complexity: `O(n)` Stack stores unmatched opening brackets up to the full length of te string.

---

## 🔥 Final Thoughts
Both approaches solve the `Valid Parentheses` problem in `O(n)` time and `O(n)` space using a stack based strategy.  
Approach1 (Hashmap): More concise and easier to scale if more types of brackets are added.  
Approach2 (Manual check): Slightly longer, but more explicit in logic.

The **hashmap** approach is the preferred due to its simplicity.  

---

## References
[LeetCode #20](https://leetcode.com/problems/valid-parentheses/description/)