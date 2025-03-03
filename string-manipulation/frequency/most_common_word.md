# Most Common Word (LeetCode #819)
**Two Input**(String: `paragraph`, String array: `banned`). **One Output**(String).  
Return the most common word that is not banned.  
There is at least one word that is not banned, and that the answer is unique.

In paragraph, case-insensitive(upper, lowercase are same) and the answer returned in `lowercase`.

**Constraints:**
> 1 <= paragraph.length <= 1000  
> 0 <= banned.length <= 100  
> 1 <= banned[i].length <= 10  
> banned[i] consists of only lowercase English letters.  
> paragraph consists of English letters, space `' '`, or `"!?',:."`.

ex1:  
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit", banned = ["hit"]  
Output: "ball"

ex2:  
Input: paragraph = "a.", banned = []  
Output: "a"

## Solution Approaches
### Way 1: re.findall & Counter
**Code:** [Most Common word with findall](most_common_findall.py)  
```python
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    # Preprocessing, Convert to lowercase and remove punctuation(`.,?!`).
    words = re.findall(r'\w+', paragraph.lower()) # Extract words only

    banned_set = set(banned) # Convert to set for O(1) lookups
    word_counts = collections.Counter(w for w in words if w not in banned_set)
    
    # Bring the one of `most_common(1)`
    return word_counts.most_common(1)[0][0]
```

### Way 2: List comprehension & Counter
**Code:** [Most Common word with List comprehension](most_common_comprehension.py)  
```python
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    # List Comprehension with regular expressions.
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
            if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
```

## 🔥 Final Thoughts
Both approaches efficiently solve the problem in `O(n)` time. Filtering banned words, using `Counter()`.  
Way 1(`re.findall`) is slightly more optimized, avoiding unnecessary whitespace handling.  
Way 2(`re.sub()` + list comprehension) is more Pythonic.  
Thus, Way 1 is generally faster and recommended way.

## References
[LeetCode #819](https://leetcode.com/problems/most-common-word/description/)
