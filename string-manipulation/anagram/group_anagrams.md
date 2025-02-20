# Group Anagrams (LeetCode #49)
Group the **anagrams** together. Return the answer in any order.  
Anagram: Same characters, in a different order.

**Constraints:**
> 1 <= strs.length <= 10^4  
> 0 <= strs[i].length <= 100  
> strs[i] is lowercase English letters.

ex1:  
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]  
Output: [["bat"], ["nat","tan"], ["ate", "eat", "tea"]]

ex2:  
Input: strs = [""]  
Output: [[""]]  

---

## Solution Approaches
### Way 1:
**Code:** [Sorted](group_anagrams_sorted.py)
```python
def groupAnagrams(strs:List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        """
            sorted(word): "a","e","t"
            ''.join: "aet"
            anagram dict {"aet": ["eat"]}
        """
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())
```

### Way 2: 
**Code:** [Frequency- Hashmap](group_anagrams_frequency.py)
```python
def groupAnagrams(strs:List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        # Create a frequency list of 26 zeros for 'a' to 'z'.
        count = [0] * 26
        for char in word:
            # ord(char) returns ASCII value.
            count[ord(char) - ord('a')] += 1
            
        # Covert list to tuple(hashtable) and use as dicts key.
        anagrams[tuple(count)].append(word)
        # *Quick Note: List is changeable, Tuple is unchangeable. 
    return list(anagrams.values())
```

## 🔥 Final Thoughts
Both approaches efficiently works to Group Anagrams.  
Way 1 `O(n*mlogm)`  
- Pros: More intuitive and easier to implement.  
- Cons: Sorting is slow when length is large, Uses extra space to store sorted word.

Way 2 `O(n*m)`
- Pros: More optimized and suitable for **large datasets**.
- Cons: Not a good idea for non-English languages. (fixed-length list 26)

## References
[LeetCode #49](https://leetcode.com/problems/group-anagrams/description/)  
[Python defaultdict Doc](https://docs.python.org/3/library/collections.html#collections.defaultdict)